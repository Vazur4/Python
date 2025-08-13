from random import randint
print("Adivina el numero")

DIFICIL = 5
FACIL = 10

def difficult():
    level = input("Choose a difficult level: hard/easy")
    if level  == "hard":
        return DIFICIL
    elif level == "easy":
        return FACIL

def answer(opcion, number, attempt):
    if opcion > number:
        print("To high")
        return attempt -1
    elif opcion < number:
        print("To low")
        return attempt -1
    elif opcion == number:
        return 0

number = randint(1,100)


def game():
    attempt = difficult()

    opcion = 0
    while opcion !=number:
        opcion = int(input(f"Turno {attempt}. Escoge el numero: "))
        attempt = answer(opcion,number,attempt)
        if attempt == 0:
            print("No hay turnos")
            break
        else:
            print("Again")
        

game()