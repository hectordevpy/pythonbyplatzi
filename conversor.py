#Hacer una calculadora de soles a dólares y de dólares a soles.

tipo_de_moneda = input("¿Tienes soles o dollars? ")
if tipo_de_moneda == "soles":
    soles = input("¿Cuántos soles tienes? ")
    soles = float(soles)
    valor_dollars = 3.95
    dollars = soles / valor_dollars
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " " + "dólares")

elif tipo_de_moneda == "dollars":
     dollars = input("¿Cuántos dollars tienes? ")
     dollars = float(dollars)
     valor_soles = 3.95
     soles = dollars * valor_soles
     soles = round(soles,2)
     soles = str(soles)
     print("Tienes S/" + soles)
else:
    tipo_de_moneda != "soles" or "dollars"
    print("¡Por favor ingresa un valor correcto!")

      