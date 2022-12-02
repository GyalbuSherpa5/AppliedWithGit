
print(f"""
    WELCOME TO SUNWAY CHARACTER CHECK SYSTEM
              MAITIDEVI, KATHMANDU
""")

detail = input("Enter the input : ")

capital = 0
small = 0
num = 0
al = 0

for i in detail:
    if i.isupper():
        capital += 1
    elif i.islower():
        small += 1
    elif i.isnumeric():
        num += 1
    elif not i.isalnum():
        al += 1
        if i.isspace():
            al -= 1


print(f"""
    
    Upper case letter : {capital}
    Lower case letter : {small}
    Special character : {al}
    Numeric data      : {num}
    
    Thank you for the visit
""")
