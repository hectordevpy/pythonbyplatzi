# def run():
#     exponente = 1
#     while exponente < 1001:
#         print("2 elevado a " + str(exponente) + " " + "es igual a " + str(2 ** exponente))
#         if exponente == 1000:
#             break
#         exponente += 1
    
    
# if __name__ == "__main__":
#     run()

def run():
    LIMITE = 1000000

    exp = 0
    potencia = 2 ** exp
    while potencia < LIMITE:
        print("2 elevado a " + str(exp) + " " + "es igual a " + str(potencia))
        exp = exp + 1
        potencia = 2 ** exp




if __name__ == "__main__":
    run()