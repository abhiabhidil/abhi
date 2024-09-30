dictionary = {1:"Apple", 2:"Banana", 3:"Orange", 4:"Peach"}

class CustomError(Exception):
    pass

def checkKey(x):
    try:
        x=int(x)
    except:
        print(f"{x} Key is not a Integer")
    try:
        if not x in dictionary.keys():
            raise ValueError(f"{x} Key is not in Dictionary")
    except ValueError as e:
        print(e)
    else:
        print(f"{x}: '{dictionary[x]}'")
    finally:
        print(dictionary)

i=1
while i==1:
    i=int(input("Do you want to insert item 0/1: "))
    if i==0:
        break
    print(i)
    x=int(input("Key: "))
    y=input("Value: ")
    dictionary.update({x:y})

inKey=input("Enter a Key: ")

checkKey(inKey)