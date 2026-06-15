#Ejercicio 3
total = 0
contador = 0
while True :
    numb = input("Enter a number :")
    if numb == "done" :
        break
    try :
        numb = int(numb)
    except :
        print("invalid input")
        continue
    total = total + numb
    contador = contador + 1
    promedio = total / contador
print("promedio", promedio)
