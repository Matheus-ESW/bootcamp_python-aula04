## iniciando aula 04 do bootcamp

## Exercício será tipar o desafio da aula 03

# nome_valido = False
# salario_valido = False
# bonus_valido = False

# while not nome_valido:
#     try:
#         nome = input("Digite seu nome: ")

#         # Verifica se o nome está vazio
#         if len(nome) == 0:
#             raise ValueError("O nome não pode estar vazio.")
#         # Verifica se há números no nome
#         elif any(char.isdigit() for char in nome):
#             raise ValueError("O nome não deve conter números.")
#         else:
#             print("Nome válido:", nome)
#             nome_valido = True
#     except ValueError as e:
#         print(e)

# # Solicita ao usuário que digite o valor do seu salário e converte para float

# try:
#     salario = float(input("Digite o valor do seu salário: "))
#     if salario < 0:
#         print("Por favor, digite um valor positivo para o salário.")
# except ValueError:
#     print("Entrada inválida para o salário. Por favor, digite um número.")
#     exit()

# # Solicita ao usuário que digite o valor do bônus recebido e converte para float
# try:
#     bonus = float(input("Digite o valor do bônus recebido: "))
#     if bonus < 0:
#         print("Por favor, digite um valor positivo para o bônus.")
# except ValueError:
#     print("Entrada inválida para o bônus. Por favor, digite um número.")
#     exit()

# bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# # Imprime as informações para o usuário
# print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

## Exercícios de Listas e Dicionários

## 1. Lista de números ao quadrado

#ex 1

# numeros = list(range(1, 11))
# for numero in numeros:
#     print(numero**2)

## 2. Modificar lista de linguagens

# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

## 3. Informações de um livro

# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")

## 4. Contar ocorrências de caracteres

# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
    
#     return contagem

# print(contar_caracteres("engenharia de dados"))

## 5. Preço total da lista de compras

# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(precos[item] for item in lista_compras)
# print(f"Preço total: {total}")

## Exercícios intermediários e mais avançados
## 6. Eliminação de Duplicatas
## Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))

# print(emails_unicos)

## 7. Filtragem de Dados
## Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades = [22, 15, 30, 17, 18]
# idades_validas = [idade for idade in idades if idade >= 18]

# print(idades_validas)

## 8. Ordenação Personalizada
## Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: Wpessoa["nome"])

# print(pessoas)

## 9. Agregação de Dados
## Objetivo: Dado um conjunto de números, calcular a média.

# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)

# print("Média:", media)

## 10. Divisão de Dados em Grupos
## Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]

# print("Pares:", pares)
# print("Ímpares:", impares)

## Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)