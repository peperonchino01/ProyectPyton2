import statistics

notas = [4.5, 6.0, 5.5, 7.0, 6.0, 5.0, 6.5]

print("=== CALCULADORA DE PROMEDIO CON LIBRERÍAS ===")
print(f"Notas ingresadas: {notas}\n")

promedio = statistics.mean(notas)
mediana = statistics.median(notas)
moda = statistics.mode(notas)

print(f"-> El promedio final es: {promedio:.2f}")
print(f"-> La nota mediana es: {mediana:.1f}")
print(f"-> La nota más repetida (moda) es: {moda:.1f}")