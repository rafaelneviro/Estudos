"""Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. 
Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. 
Note que cada valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre os números que já foram fornecidos. 
Exibir na tela o vetor final que foi digitado. 
"""
a = []
k = 0
while k <= 10:
    n = int(input("Digite um número: "))
    if n in a:
        print("Esse número já foi digitado, digite outro.")
    else:
        a.append(n)
        k += 1
print(f"Vetor: {a}")
    