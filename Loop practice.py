loop = True
while loop:
    name = input("Guess my name! :")
    if name != "Anton":
        print("That is not my name!Try again")
    else:
        print("Yes!That's my name!")
        break
