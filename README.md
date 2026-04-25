# Análise de Veículos

Este projeto é um aplicativo web desenvolvido com Streamlit para explorar dados de anúncios de veículos.

O objetivo é visualizar informações importantes do conjunto de dados, como quilometragem e preço dos veículos, usando gráficos interativos.

## Aplicação online

https://myproject-1-8thg.onrender.com

## Funcionalidades

- Visualização de um histograma da quilometragem dos veículos.
- Visualização de um gráfico de dispersão entre quilometragem e preço.
- Botões interativos para gerar os gráficos sob demanda.
- Filtro por preço máximo utilizando slider interativo.
- Análise visual de dados de veículos usados.

## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit
- Render

## Arquivos do projeto

- `app.py`: arquivo principal do aplicativo.
- `vehicles.csv`: conjunto de dados usado na análise.
- `requirements.txt`: lista de bibliotecas necessárias.
- `notebooks/EDA.ipynb`: notebook usado para análise exploratória.
- `streamlit/config.toml`: configuração do Streamlit para deploy.

## Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py