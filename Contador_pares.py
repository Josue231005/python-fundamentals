pares = 0

while True:
    numb = input("Enter a number: ")

    if numb == "done":
        break

    try:
        numb = int(numb)
    except:
        print("Invalid input")
        continue

    if numb % 2 == 0 :
        pares = pares + 1
    

print("Pares:", pares)