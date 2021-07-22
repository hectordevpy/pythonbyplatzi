def run():
    # for i in range(1000):
    #     if i % 2 != 0:
    #         continue
    #     print(i)


    # for i in range(2000):
    #     if i == 1992:
    #         break
    #     print(i)

    frase = input("Escribe una frase: ")
    for letra in frase:
        print(letra, end=(" "))
        if letra == "o":
            break
       




if __name__ == "__main__":
    run()