#EJERCICIO 1 
contador = 0
while True:
    num = input("Enter a number :")
    if num == "done" :
            break
        
    try:
            num = int(num)
    except:
            print("Invalid input")
            continue
        
    contador = contador + 1
    
print("contador: ", contador)