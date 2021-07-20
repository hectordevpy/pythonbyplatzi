def run():
    exponente = 1
    while exponente < 1001:
        print("2 elevado a " + str(exponente) + " " + "es igual a " + str(2 ** exponente))
        if exponente == 1000:
            break
        exponente += 1
    
    
if __name__ == "__main__":
    run()