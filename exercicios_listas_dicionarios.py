# Exercícios de Listas e Dicionários
# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista_numeros: list = list(range(1,11))

# for numero in lista_numeros:
#     print(numero**2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# lista: list = ["Python", "Java", "C++", "JavaScript"]

# lista.remove("C++")

# lista.append("Ruby")

# print(lista)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# livro: dict = {
#     "Titulo": "O Homem Mais Rico da Babilônia",
#     "Autor": "George S. Clason",
#     "Ano": "1926"
# }

# for k, v in livro.items():
#     print(f"{k}: {v}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# palavra: str = "Engenharia de dados"
# palavra_formatada: str = palavra.lower()

# contagem_caracteres: dict = {}

# for letra in palavra_formatada:
#     contagem_caracteres[letra] = contagem_caracteres.get(letra, 0) + 1

# print(contagem_caracteres)


# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# lista_compras: list = ["maçã", "banana", "cereja"]

# precos: dict = {
#     "maçã": 0.45, 
#     "banana": 0.30, 
#     "cereja": 0.65
# }

# valor_total: float = 0
# for item in lista_compras:
#     valor_total += precos[item]

# print(f"O valor total da lista de compras é R$ {valor_total}")

# # Outra forma

# total = sum(precos[item] for item in lista_compras)

# print(f"Preço total: {total}")

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))

# print(emails_unicos)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades: list = [1,34,14,13,11,18,19,25]

# idades_filtrada: list = [idade for idade in idades if idade >= 18]

# print(idades_filtrada)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "Carol", "idade": 30},
#     {"nome": "Alice", "idade": 25},
#     {"nome": "Bob", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])

# print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# numeros: list = [2, 33, 21, 10, 30, 55]

# media = sum(numeros) / len(numeros)

# print(media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# numeros: list = [2, 33, 21, 10, 30, 55, 3]

# numeros_pares: list = [numero for numero in numeros if numero % 2 == 0]
# numeros_impares: list = [numero for numero in numeros if numero % 2 != 0]

# print(f"Números pares: {numeros_pares}")
# print(f"Números ímpares: {numeros_impares}")

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# produtos: list = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# Atualizar o preço do produto com id 2 para 90

# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90

# print(produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1: dict = {"a": 1, "b": 2}
# dicionario2: dict = {"c": 3, "d": 4}

# # Forma 1:
# dicionario_completo: dict = dicionario1 | dicionario2

# # Forma 2: 
# # dicionario_completo: dict = {**dicionario1, **dicionario2}

# print(dicionario_completo)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo: dict = {}
# for item, saldo in estoque.items():
#     if saldo > 0:
#         estoque_positivo[item] = saldo

# print(estoque_positivo)

# Forma 2
# estoque_positivo: dict = {item: saldo for item, saldo in estoque.items() if saldo > 0}
# print(estoque_positivo)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# dicionario = {"a": 1, "b": 2, "c": 3}

# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

# print("Chaves:", chaves)
# print("Valores:", valores)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# texto: str = "engenharia de dados"

# caracteres: dict = {}

# for caractere in texto:
#     caracteres[caractere] = caracteres.get(caractere, 0) + 1

# print(caracteres)