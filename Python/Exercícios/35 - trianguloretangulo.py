#Leia os catetos de um triângulo retangulo e imprima sua hipotenusa. 
cateto1 = float(input("Cateto 1: "))
cateto2 = float(input("Cateto 2: "))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print(f"Hipotenusa: {hipotenusa}")
