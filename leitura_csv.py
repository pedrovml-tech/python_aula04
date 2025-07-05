import csv


# Caminho para o arquivo
caminho_arquivo: str = "exemplo.csv"

# Inicializar lista vazia para armazenar os dados do arquivo
dados: list = []

# Utilizar o gerenciador de contexto `with` para abrir/fechar o arquivo:
with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    # Criar objeto de leitor de CSV
    leitor_csv: csv.DictReader = csv.DictReader(arquivo)

    # Iterar cada linha do arquivo
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

for linha in dados:
    print(linha)
