import pandas as pd



def organize_column(document, column):  # Função que organiza a tabela e capitaliza se a coluna for string
    document.sort_values(column)

    for i, row in enumerate(document):
        document[column] = document[column].str.capitalize()

    document.to_csv('DadosOrganizadosCRM.csv', index=False)

    return document


def filter_position(document, filter_word):  # Função que filtra por valor que contém na coluna e
    # ainda me gera um csv com os dados separados
    document.sort_values("Cargo")
    positions = pd.DataFrame()

    for i, row in enumerate(document):
        if row:
            positions = document[document['Cargo'].str.contains(f'{filter_word}')]

    positions.to_csv('PositionFilter.csv', index=False)
    return positions


def change_position(document, filter_word, word_change):  # Muda os valores filtrados pelo que foi estabelecido
    document.sort_values("Cargo")
    positions = pd.DataFrame()

    for i, row in enumerate(document):
        if row:
            positions = document[document['Cargo'].str.contains(f'{filter_word}')]
            positions.loc[i:i] = word_change

    positions.to_csv('filtrate.csv', index=False)
    return positions

