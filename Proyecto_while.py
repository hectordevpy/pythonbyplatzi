def run():
    menu = '''
    Hola, María Fe. 💚
    En este juego aprenderás matemáticas con Papá. 🙋
    SI RESPONDES BIEN HABRÁ UNA SORPRESA. 🐇
    1. Suma
    2. Resta
    Por favor escoge un número: '''

    opcion = int(input(menu))
    while opcion != 1 and opcion != 2:
        print("Ups! Escoge un número correcto 😖 ")
        opcion = int(input(menu))
        continue
    if opcion == 1:
        print("Buena elección ¡vamos a sumar! 😎")
        numero1 = int(input("Ingresa el primer número: ")) 
        numero2 = int(input("Ingresa el segundo número: "))
        respuesta1 = int(input("¿Cuál es el resultado de la suma?: "))
        while respuesta1 != numero1 + numero2:
            print("Intenta otra vez, tú puedes 💪")
            respuesta1 = int(input("¿Cuál es el resultado de la suma?: "))
            continue
        if respuesta1 == numero1 + numero2:
            print("¡Felicidades! ¡Lo lograste! 🥳")
            import pywhatkit as rep
            rep.playonyt("Sunny Bunnies Characters In Real Life")        
    elif opcion == 2:
        print("Excelente elección ¡vamos a restar!😎 ")
        numero1 = int(input("Ingresa el primer número: ")) 
        numero2 = int(input("Ingresa el segundo número: "))
        respuesta2 = int(input("¿Cuál es el resultado de la resta?: "))
        while respuesta2 != numero1 - numero2:
            print("Intenta otra vez, tú puedes 💪")
            respuesta2 = int(input("¿Cuál es el resultado de la resta?: "))
        if respuesta2 == numero1 - numero2:
            print("¡Felicidades! ¡Lo lograste! 🥳")
            import pywhatkit as rep
            rep.playonyt("Sunny Bunnies Characters In Real Life") 

if __name__ == '__main__':
    run()