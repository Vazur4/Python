def find_highest_binder(participantes):
    """"Find the highest """
    mayor = 0
    winner = ""
    for key in  participantes:
        if participantes[key] > mayor:
            mayor = participantes[key]
            winner = key;


    print(f"The winner is {winner} with: {mayor}")




participantes = {}


conti =  False

while  not conti:
    name =  input("What is  your name?: ")
    blind = int(input("What's your bid: ")
)
    participantes[name] = blind

    c = input("Do you want continue? (yes/no): ")
    if c.lower() in "no":
        conti  = True

    elif c.lower() in "yes":
        print("\n"*20)

find_highest_binder(participantes)

