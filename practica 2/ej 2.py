numero = int(input("ingrese un numero "))
par = (numero%2 == 0)
if numero > 0:
    if par:
        print(numero, " es positivo y par") 
    else: 
            print(numero, "es positivo e impar")
elif numero < 0:
    if par:
            print(numero, " es negativo y par")
    else:
            print(numero, " es negativo e impar")
else:
        print(numero, " es 0 y por lo tanto par")