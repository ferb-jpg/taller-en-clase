#ejercicio1
capital1 = float(input("Ingrese el capital que desea invertir: "))

tasa_anual = 0.15
tasa_mensual = (1 + tasa_anual) ** (1 / 12) - 1

ganancia = capital1 * tasa_mensual
total = capital1 + ganancia

print(f"Ganancia: {ganancia:.2f}")
