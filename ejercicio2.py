#ejercicio2
sueldo_base = float(input("Ingrese su sueldo: "))
if sueldo_base <= 0:
    print("El sueldo base debe ser un número positivo")

venta1 = float(input("Ingrese el valor de la venta 1: "))
venta2 = float(input("Ingrese el valor de la venta 2: "))
venta3 = float(input("Ingrese el valor de la venta 3: "))

comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

total_comisiones = comision1 + comision2 + comision3
total = total_comisiones + sueldo_base

print("Comisión de la venta 1:", comision1)
print("Comisión de la venta 2:", comision2)
print("Comisión de la venta 3:", comision3)
print("Total comisiones:", total_comisiones)
print("Total:", total)
