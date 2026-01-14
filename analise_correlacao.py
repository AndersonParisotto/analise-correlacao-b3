#dados do Yahoo Finance
import yfinance as yf
#complemento para gráficos
import seaborn as sns
#gráficos
import matplotlib.pyplot as plt
#receber e organizar dados
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#lista de ativos
#PETR4.SA = Petrobras
#VALE3.SA = Vale
#ITUB4.SA = Itaú
#^BVSP = Índice Bovespa
ativos = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "^BVSP"]

#período de análise
inicio = "2023-01-01"
fim = "2025-01-14"  

print(f"Baixando dados de {inicio} até {fim}...")

#download com tratamento de erros
try:
    dados = yf.download(ativos, start=inicio, end=fim, progress=False)
    
    #verifica se conseguiu baixar dados
    if dados.empty:
        raise ValueError("Nenhum dado foi baixado. Verifique a conexão.")
    
    #seleciona apenas Adj Close
    if 'Adj Close' in dados.columns.levels[0]:
        df = dados['Adj Close']
    else:
    #fallback para Close se Adj Close não existir
        df = dados['Close']  
    
    print(f"✓ Dados baixados com sucesso! Shape: {df.shape}")
    
except Exception as e:
    print(f"✗ Erro no download: {e}")
    raise

#limpeza de dados
#remove linhas onde TODOS os ativos estão nulos
df = df.dropna(how='all')

#preenche valores faltantes com forward fill
df = df.ffill()

#verifica se ainda há dados após limpeza
if df.empty:
    print("✗ Erro: DataFrame vazio após limpeza.")
else:
    print(f"✓ Dados limpos. Shape final: {df.shape}")
    
    #cálculo de retornos diários
    retornos = df.pct_change().dropna()
    
    print(f"✓ Retornos calculados. Shape: {retornos.shape}")
    
    #matriz de correlação
    correlacao = retornos.corr()
    
    print("\n📊 Matriz de Correlação:")
    print(correlacao.round(2))
    
    #visualização
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        correlacao, 
        annot=True, 
        cmap='coolwarm', 
        fmt=".2f", 
        vmin=-1, 
        vmax=1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8}
    )
    plt.title(f"Matriz de Correlação de Ativos ({inicio} a {fim})", fontsize=14, pad=20)
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Análise concluída com sucesso!")

    #cálculo do Retorno Acumulado
    #(1 + retorno_diario).cumprod() calcula o crescimento de R$ 1 ao longo do tempo
    retorno_acumulado = (1 + retornos).cumprod()

    #plotando a performance
    plt.figure(figsize=(12, 6))
    for coluna in retorno_acumulado.columns:
        plt.plot(retorno_acumulado.index, retorno_acumulado[coluna], label=coluna)

    plt.title("Evolução de R$ 1,00 Investido (Retorno Acumulado)", fontsize=14) 
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
