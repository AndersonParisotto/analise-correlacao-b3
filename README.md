Análise de Correlação: Ativos da B3 vs Ibovespa

Este projeto analisa a relação estatística entre grandes ativos da bolsa brasileira (Petrobras, Vale e Itaú) em comparação ao principal índice do mercado (Ibovespa).
Com o objetivo é identificar como esses ativos se movem em relação ao mercado geral, auxiliando na compreensão de risco e diversificação de carteira para o período de 2023 a 2025.

Tecnologias Utilizadas
- Python 3.x
- Pandas: Manipulação e limpeza de dados financeiros.
- YFinance: Extração de dados reais via API do Yahoo Finance.
- Seaborn & Matplotlib: Visualização de dados e criação do Heatmap de correlação.

O que os dados dizem?
- Alta Correlação: O Itaú (ITUB4) demonstrou a maior proximidade com o Ibovespa (0.74), sendo um forte pilar do índice.
- Independência: A Petrobras (PETR4) apresentou uma correlação moderada (0.48), indicando que fatores específicos (como preço do barril ou decisões políticas) afetaram seu preço de forma distinta do resto do mercado.
- Oportunidade de Diversificação: A correlação entre Vale e Petrobras é baixa (0.21), o que sugere que ter ambas na carteira pode ajudar a reduzir o risco sistêmico.

Como executar
1. Instale as dependências: `pip install -r requirements.txt` (opcional)
2. Execute o script: `python analise_correlacao.py`
