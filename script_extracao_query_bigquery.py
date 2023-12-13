# Instalar as bibliotecas somente na primeira execução
# pip install google-cloud-storage
# pip install google-cloud-bigquery
# pip install pandas as pd
# pip install pandas-gbq
# pip install db-dtypes


import db_dtypes
import pandas as pd
from google.cloud import bigquery

# Passar o caminho que as credenciais estão salvas
ambiente_01 = 'C:/pasta/credencial_amb_01.json'
ambiente_02 = 'C:/pasta/credencial_amb_02.json'

# Alterar o ambiente se for necessário (ambiente_01, ambiente_02)
client = bigquery.Client.from_service_account_json(ambiente_01)

query = """
SELECT
  col01,
  col02,
  col03
FROM `nome_da_tabela`
WHERE col01 = 'filtro'

"""

results_df = client.query(query).to_dataframe(progress_bar_type='tqdm')

# Quantidade de linhas e colunas
results_df.shape

# Exporta os dados em excel - obs. Alterar o nome do arquivo conforme necessidade
results_df.to_excel('C:/pasta/output/nome_do_arquivo.xlsx')
