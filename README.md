Este projeto realiza a análise de um conjunto de dados meteorológicos fornecido em um arquivo CSV.
O foco é analisar precipitação, temperatura máxima, temperatura mínima e temperatura média, além de gerar visualizações gráficas.

Tecnologias Utilizadas

Python 3.x

Pandas — Manipulação de dados

Matplotlib — Geração de gráficos

Virtual Environment (venv) — Ambiente isolado de pacote

 Como Executar o Projeto
1️ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate     # Windows

2️ Instalar as dependências
pip install pandas matplotlib

3️ Executar o script
python analise_meteorologica.py

 O que o script faz?

 Lê o arquivo CSV
 Limpa e organiza os dados
 Calcula estatísticas importantes
 Gera gráficos:

Precipitação ao longo do tempo

Temperatura máxima

Temperatura mínima

Temperatura média

 Exemplo de Gráficos:

O script gera gráficos automaticamente, como por exemplo:

 Variação da precipitação

 Temperaturas máximas e mínimas

 Temperatura média
