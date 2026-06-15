positivos = 0
while True :
    numb = input("Enter a number :")
    if numb == "done" :
        break
    try :
        numb = int(numb)
    except :
        print("Invalid Imput")
        continue
    if numb > 0 :
        positivos = positivos + 1
print("positivos", positivos)