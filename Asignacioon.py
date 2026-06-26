class CalculadoraPromedios:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        if 1.0 <= nota <= 7.0:
            self.notas.append(nota)
        else:
            print("Error: la nota debe estar entre 1.0 y 7.0")

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"\nNotas ingresadas: {self.notas}")
        print(f"Promedio: {promedio:.2f}")

        if promedio >= 4.0:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")


calculadora = CalculadoraPromedios()

cantidad = int(input("¿Cuántas notas desea ingresar? "))

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    calculadora.agregar_nota(nota)

calculadora.mostrar_resultado()