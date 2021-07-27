def run():
    porcentaje_inmunizacion = {
        "Lima" : 54.9,
        "Ayacucho" : 61.2,
        "Cajamarca" : 51.3,
        "Arequipa" : 75.6,
        "Tacna" : 52.8,
    }
    for ciudad, porcentaje in porcentaje_inmunizacion.items():
        print(ciudad + " tiene " + str(porcentaje) + "% " + "de su población inmunizada 🥳"  )
if __name__ == "__main__":
    run()