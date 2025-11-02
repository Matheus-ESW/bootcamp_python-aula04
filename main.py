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

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# # Atualizar o preço do produto com id 2 para 90
# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90

# print(produtos)

## 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

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

# texto = "engenharia de dados"
# frequencia = {}

# for caractere in texto:
#     if caractere in frequencia:
#         frequencia[caractere] += 1
#     else:
#         frequencia[caractere] = 1

# print(frequencia)

# 3.Lendo arquivos
# Para ler um arquivo CSV em Python utilizando o módulo nativo, você pode usar a combinação
# do comando with open... para abrir o arquivo e o método .reader() do módulo csv para ler o
# arquivo linha por linha. O uso de with assegura que o arquivo será fechado corretamente após
# sua leitura, mesmo que ocorram erros durante o processo. Abaixo está um exemplo básico de
# como realizar essa operação:

# import csv

# # Caminho para o arquivo CSV
# caminho_arquivo = 'csv/uber-raw-data-sep14.csv'

# # Inicializa uma lista vazia para armazenar os dados
# dados = []

# # Usa o gerenciador de contexto `with` para abrir o arquivo
# with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
#     # Cria um objeto leitor de CSV
#     leitor_csv = csv.DictReader(arquivo)
    
#     # Itera sobre as linhas do arquivo CSV
#     for linha in leitor_csv:
#         # Adiciona cada linha (um dicionário) à lista de dados
#         dados.append(linha)

# # Exibe os dados lidos do arquivo CSV
# cont = 1
# for registro in dados:
#     if cont < 100:
#         print(registro)
#     cont += 1

# 4. Funções
# Importância na Engenharia de Dados
# Funções permitem modularizar e reutilizar código, essencial para processar e analisar 
# grandes conjuntos de dados. Na engenharia de dados, funções são usadas para encapsular 
# lógicas de transformação, limpeza, agregação e análise de dados, tornando o código mais 
# organizado e mantendo a qualidade do código.

# As funções em programação são abstrações poderosas que permitem encapsular blocos de 
# código para realizar tarefas específicas. Elas servem não apenas para organizar o código
# e torná-lo mais legível, mas também para abstrair complexidades, permitindo que os 
# programadores pensem em problemas em um nível mais alto. Uma função bem projetada pode 
# ser vista como um "mini-programa" dentro de um programa maior, com sua própria lógica e dados de entrada e saída.

# Um exemplo clássico dessa abstração é a ordenação de uma lista. Vamos primeiro desenvolver 
# uma função simples em Python que ordena uma lista usando o algoritmo de ordenação por seleção,
# um método simples mas eficaz para listas pequenas e médias. Em seguida, mostraremos como essa 
# tarefa pode ser realizada de forma mais direta usando o método sort() built-in do Python, que 
# é uma abstração fornecida pela linguagem para realizar a mesma tarefa.

# Função de Ordenação Personalizada

# # Implementação do algoritmo de ordenação por seleção

# lista = [64, 34, 25, 12, 22, 11, 90]

# for i in range(len(lista)):
#     for j in range(i+1, len(lista)):
#         if lista[i] > lista[j]:
#             lista[i], lista[j] = lista[j], lista[i]

# # Ordenando a lista
# print("Lista ordenada com função personalizada:", lista)

# Usando o Método Built-in sort()
# O Python fornece uma abstração poderosa através do método sort(), 
# que pode ordenar listas in-place de maneira eficiente e com uma sintaxe simples.

# Lista de exemplo
# lista_exemplo = [64, 34, 25, 12, 22, 11, 90]

# # Ordenando a lista com sort()
# lista_exemplo.sort()

# print("Lista ordenada com método built-in:", lista_exemplo)

# Exemplo: Transformação de Dados com Funções
# Suponhamos a necessidade de limpar e transformar nomes de usuários em um conjunto de dados.
# Uma função dedicada pode ser implementada para essa tarefa.

# def normalizar_nome(nome: str) -> str:
#     return nome.strip().lower()

# nomes = [" Alice ", "BOB", "Carlos"]
# nomes_normalizados = [normalizar_nome(nome) for nome in nomes]
# print(nomes_normalizados)

# Exercícios de Funções
# 16 - Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

# def somaLista(numeros: int) -> int:
#     somaNumeros = 0
#     for numero in numeros:
#         somaNumeros += numero

#     return somaNumeros

# numeros = [5, 12, 6, 25, 55, 107]
# somaNumeros = somaLista(numeros)
# print(somaNumeros)
# # ------------------------------------
# numeros = [5, 12, 6, 25, 55, 107]
# print(sum(numeros))

# 17 - Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def primo(numero: int):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("informe um número: "))
print(primo(numero))

# Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as 
# combinações de pares na lista que somem ao número dado.
# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
# O padrão de nomeação de funções em Python segue convenções que são amplamente aceitas pela comunidade Python, 
# conforme recomendado no PEP 8, o guia de estilo para a codificação em Python. Adotar esses padrões não só melhora a
# legibilidade do código, mas também facilita a compreensão e a manutenção por outros desenvolvedores, incluindo aqueles novos ao projeto.