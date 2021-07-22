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
        respuesta1 = int(input("¿Cuánto es 10 + 8?: "))
        while respuesta1 != 18:
            print("Intenta otra vez, tú puedes 💪")
            respuesta1 = int(input("¿Cuánto es 10 + 8?: "))
            continue
        if respuesta1 == 18:
            print("¡Felicidades lo lograste! 🥳")
            import pywhatkit as rep
            rep.playonyt("Sunnie Bunnies - Last cap")        
    elif opcion == 2:
        print("Excelente elección ¡vamos a restar!😎 ")
        respuesta2 = int(input("¿Cuánto es 8 - 3?: "))
        while respuesta2 != 5:
            print("Intenta otra vez, tú puedes 💪")
            respuesta2 = int(input("¿Cuánto es 8 - 3: "))
        if respuesta2 == 5:
            print("¡Felicidades lo lograste! 🥳")
            import pywhatkit as rep
            rep.playonyt("Sunnie Bunnies - Last cap") 

if __name__ == '__main__':
    run()