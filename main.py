import math


class ConversorAngulos:
    def __init__(self, valor=None):
        self.valor = valor

    def grados_a_radianes(self, grados):
        return grados * (math.pi / 180)

    def radianes_a_grados(self, radianes):
        return radianes * (180 / math.pi)


print("Seleccione el tipo de conversión:")
print("1. De grados a radianes")
print("2. De radianes a grados")

opcion = int(input("Ingrese 1 o 2: "))

conversor = ConversorAngulos()

if opcion == 1:
    grados = float(input("Ingrese el valor en grados: "))
    radianes = conversor.grados_a_radianes(grados)
    print(f"{grados} grados equivalen a {radianes:.6f} radianes.")

elif opcion == 2:
    radianes = float(input("Ingrese el valor en radianes: "))
    grados = conversor.radianes_a_grados(radianes)
    print(f"{radianes} radianes equivalen a {grados:.6f} grados.")

else:
    print("Opción no válida.")
