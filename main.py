import pandas as pd
import utils as u

excel_file = pd.read_excel("DadosCRM.xlsx")
u.organize_column(excel_file, "Cargo") # Organiza o documento e me gera um documento csv a parte

df = pd.read_csv("DadosOrganizadosCRM.csv") # Cria um dataframe a partir do documento criado

print(u.filter_position(df, "Auxiliar")) # Faz a filtragem de cargos usando o documento organizado

