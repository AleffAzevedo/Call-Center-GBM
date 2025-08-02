# Projeto de Previsão de Indicadores de Call Center com Gradient Boosting

Este projeto demonstra a aplicação de um modelo de Gradient Boosting para prever o numerador e o denominador de indicadores de performance de um call center, como CSAT (Customer Satisfaction Score), Nota de Qualidade e TMA (Tempo Médio de Atendimento). A previsão é baseada em dados de data e outras variáveis categóricas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
call_center_gbm/
├── data/
│   ├── call_center_data.csv
│   └── generate_data.py
├── notebooks/
│   ├── Gradient_Boosting_Call_Center.ipynb
│   └── gradient_boosting_model.py
└── README.md
```

- **data/**: Contém a base de dados fictícia (`call_center_data.csv`) e o script Python (`generate_data.py`) para gerá-la.
- **notebooks/**: Contém o Jupyter Notebook (`Gradient_Boosting_Call_Center.ipynb`) com a análise exploratória, o desenvolvimento do modelo e a avaliação dos resultados. Inclui também o script Python (`gradient_boosting_model.py`) com a lógica do modelo.
- **README.md**: Este arquivo, com a descrição do projeto.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd call_center_gbm
   ```

2. **Instale as dependências:**

   ```bash
   pip install pandas scikit-learn jupyter
   ```

3. **Execute o Jupyter Notebook:**

   ```bash
   jupyter notebook notebooks/Gradient_Boosting_Call_Center.ipynb
   ```

   No notebook, você pode executar todas as células para gerar os dados, treinar o modelo e visualizar os resultados.

## Metodologia

1. **Geração de Dados:** Foi criada uma base de dados fictícia com informações de data, login de agentes, indicadores, numerador, denominador e grupo de agentes.

2. **Pré-processamento:**
   - A coluna de data foi convertida para o formato datetime.
   - Foram extraídas features de tempo (ano, mês, dia do mês, dia da semana).
   - As variáveis categóricas (login, nome do indicador, grupo de agente) foram codificadas usando `LabelEncoder`.

3. **Modelagem:**
   - Foram treinados dois modelos de `GradientBoostingRegressor`, um para prever o numerador e outro para o denominador.
   - Os dados foram divididos em conjuntos de treino (80%) e teste (20%).

4. **Avaliação:**
   - O desempenho dos modelos foi avaliado utilizando as métricas de Erro Quadrático Médio (MSE) e R² Score.

## Resultados

Os resultados da avaliação dos modelos no conjunto de teste foram os seguintes:

- **Modelo para Numerador:**
  - MSE: 35406.36
  - R² Score: 0.72

- **Modelo para Denominador:**
  - MSE: 1293.71
  - R² Score: 0.56

As visualizações no notebook mostram a relação entre os valores reais e os valores previstos, indicando um bom ajuste do modelo para o numerador e um ajuste razoável para o denominador.

## Próximos Passos

- Otimizar os hiperparâmetros do modelo de Gradient Boosting para melhorar a performance.
- Utilizar dados reais para validar e aprimorar o modelo.
- Explorar outras features que possam influenciar os indicadores de call center.


