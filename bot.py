import requests
import openpyxl

# Função para obter dados do CNPJ
def obter_dados_cnpj(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# CNPJ para consultar
cnpj = '05529147000197'

# Obter dados do CNPJ
dados_cnpj = obter_dados_cnpj(cnpj)

# Processar os dados
if dados_cnpj:
    processed_data = [
        ['Nome', dados_cnpj['nome']],
        ['CNPJ', dados_cnpj['cnpj']],
        ['Data de Abertura', dados_cnpj['abertura']]
    ]

    # Salvar os dados em um arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Inserir os dados na planilha
    for row in processed_data:
        sheet.append(row)

    # Salvar o arquivo Excel
    workbook.save('dados_2q2.xlsx')
    print("Dados salvos com sucesso!")
else:
    print("Não foi possível obter os dados do CNPJ.")
