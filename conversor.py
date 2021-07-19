menu = """ Hola, este es tu conversor de monedas* $_$
    ¿Quieres saber a cuanto equivale la moneda de tu país en dólares?**
    ¡Este este conversor te servirá de mucho!
    *Aplica para soles peruanos, pesos argentinos y pesos colombianos.
    **También puede convertir de dólares a las monedas antes mencionadas.
    1 - Soles
    2 - Dólares
    3 - Pesos Argentinos
    4 - Pesos Colombianos
    Elige una opción: """
opcion = input(menu)
if opcion == "1":
    soles = input("¿Cuántos soles tienes? ")
    soles = float(soles)
    valor_dollars = 3.95
    dollars = soles / valor_dollars
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " " + "dólares")
elif opcion == "2":
     dollars = input("¿Cuántos dollars tienes? ")
     dollars = float(dollars)
     valor_soles = 3.95
     soles = dollars * valor_soles
     soles = round(soles,2)
     soles = str(soles)
     valor_pesos_argentinos = 96.16
     pesos_argentinos = dollars * valor_pesos_argentinos
     pesos_argentinos = round(pesos_argentinos,2)
     pesos_argentinos = str(pesos_argentinos)
     valor_pesos_colombianos = 3817.60
     pesos_colombianos = dollars * valor_pesos_colombianos
     pesos_colombianos = round(pesos_colombianos,2)
     pesos_colombianos = str(pesos_colombianos)
     print("Tienes S/" + soles + " " + "y " 
     " " + pesos_argentinos + " " + "Pesos Argentinos " + "además "
      + " " + pesos_colombianos + " " + "Pesos Colombianos")
elif opcion == "3":
    pesos_argentinos = input("¿Cuántos pesos tienes? ")
    pesos_argentinos = float(pesos_argentinos)
    valor_dollars = 96.16
    dollars = pesos_argentinos / valor_dollars
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " " + "dólares")
elif opcion == "4":
    pesos_colombianos = input("¿Cuántos pesos tienes? ")
    pesos_colombianos = float(pesos_colombianos)
    valor_dollars = 3817.60
    dollars = pesos_colombianos / valor_dollars
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " " + "dólares")
else:
    print("¡Por favor ingresa un valor correcto!") 