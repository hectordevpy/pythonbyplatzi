def conversor_to_dollars(tipo_moneda, valor_dollars):
    tipo_moneda = input("¿Cuántos " + tipo_moneda + " tienes?: ")
    tipo_moneda = float(tipo_moneda)
    dollars = tipo_moneda / valor_dollars
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " " + "dólares")

def conversor_to_localmoney(tipo_moneda, valor_soles, valor_argentinos, valor_colombianos):
    tipo_moneda = input("¿Cuántos " +  tipo_moneda +  "tienes?: ")
    tipo_moneda = float(tipo_moneda)
    soles = tipo_moneda * valor_soles
    soles = round(soles,2)
    soles = str(soles)
    argentinos = tipo_moneda * valor_argentinos
    argentinos = round(argentinos,2)
    argentinos = str(argentinos)
    colombianos = tipo_moneda * valor_colombianos
    colombianos = round(colombianos,2)
    colombianos = str(colombianos)
    print("Tienes PEN " + soles + " " + "que equivale a " 
    " " + argentinos + " " + "ARS " + "y a su vez "
    + " " + colombianos + " " + "COP")
menu = """ Hola, este es tu conversor de monedas FuckMoney $_$
    ¿Quieres saber a cuánto equivale la moneda de tu país en dólares o viceversa?*
    ¡Este este conversor te servirá de mucho!
    *Aplica para soles peruanos, pesos argentinos y pesos colombianos.
    1 - Soles
    2 - Dólares
    3 - Pesos Argentinos
    4 - Pesos Colombianos
    Elige una opción: """
opcion = input(menu)
if opcion == "1":
    conversor_to_dollars("soles", 3.95) 
elif opcion == "2":
     conversor_to_localmoney("dólares ", 3.95, 96.20, 3817.60)
elif opcion == "3":
    conversor_to_dollars("pesos argentinos", 96.20)
elif opcion == "4":
    conversor_to_dollars("pesos colombianos", 3817.60)
else:
    print("¡Por favor ingresa un valor correcto!") 