import random
#Debo programar para que la computadora elija un número 
#aleatorio y pueda dar algunas pistar para que el usuario
#adivine cuál es.

def run():
    numero = random.randint(0, 100)
    numero_random = int(input("Elige un número: "))
    while numero_random != numero:
        if numero_random > numero:
            print("Elige un número menor. 😋")
        if numero_random < numero:
            print("Elige un número mayor. 😌")
        numero_random = int(input("Elige un número: "))
    if numero_random == numero:
        print("¡GANASTE!🥳 ")




if __name__ == "__main__":
    run()