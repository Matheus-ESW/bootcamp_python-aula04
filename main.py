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

livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")