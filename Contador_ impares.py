#Ejercicio 5
impares = 0

while True:
    numb = input("Enter a number: ")

    if numb == "done":
        break

    try:
        numb = int(numb)
    except:
        print("Invalid input")
        continue

    if (numb + 1) % 2 == 0 :
        impares = impares + 1
    

print("impares:", impares)