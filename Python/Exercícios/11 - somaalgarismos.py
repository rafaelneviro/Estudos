"""Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
"""
num = input("Digite um número: ")
soma = 0
for x in num:
    soma += int(x)
print(f"Soma = {soma}")
