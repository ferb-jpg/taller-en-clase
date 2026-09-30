#ejercicio5
pesos = float(input("Ingrese la cantidad de pesos: "))
if pesos <= 0:
    print("La cantidad de pesos debe ser un número positivo")
dolar = float(input("Ingrese el valor del dolar: "))

conversion = pesos / dolar
print(f"La cantidad de dolares que puede comprar es: {conversion:.2f}")