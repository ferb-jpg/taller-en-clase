presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temp = float(input("Ingrese la temperatura: "))

masa = (presion * volumen) / (0.37 * (temp + 460))

print(f"La masa es: {masa:.2f}")