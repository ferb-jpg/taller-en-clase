#ejercicio4
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) /3

nota4 = float(input("Ingrese la nota del parcial final: "))
nota5 = float(input("Ingrese la nota del trabajo final: "))

nota_final = (promedio * 0.40) + (nota4 * 0.50) + (nota5 * 0.10)
print(f"\nCalificación final: {nota_final:.2f}")
if nota_final >= 3.0:
    print("Aprobó")
else:
    print("Reprobó")
