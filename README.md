# Organizador simples de excel

Um pequeno script em python que organiza um arquivo excel.

## Instalação

Abra o terminal do seu computador e digite o comando abaixo:
 
```bash
git clone https://github.com/joaovitorsh/script-organizar-excel.git
```

Logo após fazer um clone do projeto em seu computador digite o comando a baixo para rodar

```bash
python main.py
```

## Exemplo de uso

Recomendo fazer o uso pelo arquivo main.py em um editor de texto ou ide. :)

```python
import pandas as pd
import utils as u

excel_file = pd.read_excel("DadosCRM.xlsx") # Cria um dataframe com o excel original

u.organize_column(excel_file, "Cargo") # Organiza o documento e me gera um documento csv a parte

df = pd.read_csv("DadosOrganizadosCRM.csv") # Cria um dataframe a partir do documento criado

print(u.filter_position(df, "Auxiliar")) # Faz a filtragem de cargos usando um parâmetro de pesquisa e o documento organizado
```

## Contribuição
Pull requests são bem-vindas. Para maiores mudanças, por favor abra uma issue e deixe a sua sugestão de mudança.


## Licença
[MIT](/LICENSE)
