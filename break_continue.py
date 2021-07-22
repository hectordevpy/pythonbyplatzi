def run():
    # for i in range(1000):
    #     if i % 2 != 0:
    #         continue
    #     print(i)


    # for i in range(2000):
    #     if i == 1992:
    #         break
    #     print(i)

    # frase = input("Escribe una frase: ")
    # for letra in frase:
    #     print(letra, end=(" "))
    #     if letra == "o":
    #         break

    
    print("Resuelve la adivinanza. Tienes 5 intentos ")
    intentos = 0
    while intentos < 3:
        palabra = input("Blanco por dentro, verde por fuera ¿Qué es?: ")
        intentos += 1
        if palabra == "Pera":
            print("¡Adivinaste!")
            break
        if intentos == 3:
            print("End Game!")
            
        
    
       




if __name__ == "__main__":
    run()