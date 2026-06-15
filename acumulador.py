#Ejercicio 2
total = 0
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
print (total)