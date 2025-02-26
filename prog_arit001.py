'''
Programa: Soma
Descrição: determine o n-´esimo termo e a soma dos termos de uma progress˜ao aritm´etica onde n,
primeiro termo e a raz˜ao s˜ao dados pelo usu´ario.
Autor: Arthur Gaspareto
Data: 25/02/25
Versão: 0.0.1
Novidades da Versão

25/02/2025
Nesta versão:
1.
'''

#Alocação de Memória
termo_1 = 0
razao = 0
n = 0

#Entrada de Dados

termo_1 = float(input("Qual o primeiro termo?"))
razao = float(input("Qual a razão?"))
n = float(input("Qual o n desejado?"))

#Processamento de Dados
termo_geral = termo_1 + (n-1)*razao

#Saída de dados

print(f'O valor do termo desejado é: {termo_geral}.')