def run():
    numero = int(input("Ingresa un número: "))
    esPrimo = True
    for i in range(2, numero):
        if numero % i == 0:
            esPrimo = False
    if numero == 1:
        print("No es número primo")
    elif esPrimo:
        print("Es número primo")
    else:
        print("No es número primo")

if __name__ == '__main__':
    run()
    