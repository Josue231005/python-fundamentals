#Ejercicio 6
Largest = None
Smallest = None
while True :
    numb = input("Enter a number :")
    if numb == "done" :
        break
    try:
        numb = int(numb)
    except :
        print ("invalid input")
        continue
    if Largest is None or numb > Largest :
        Largest = numb
    if Smallest is None or numb < Smallest :
        Smallest = numb
print ("Maximun is", Largest)
print ("Minimum is", Smallest)