import random
import math

print("==========================================")
print("CÁLCULO DE AREAS POR MÉTODO DE MONTECARLO")
print("==========================================")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios a generar: "))

puntosElipse = 0
puntosIntersec = 0

for _ in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

    if (x**2 / a**2) + (y**2 / b**2) <= 1:
        puntosElipse += 1
            
        if (x**2 / c**2) - (y**2 / d**2) >= 1:
            puntosIntersec += 1

areaElipse = math.pi * a * b

if puntosElipse > 0:
    areaIntersec = areaElipse * (puntosIntersec / puntosElipse)
else:
    areaIntersec = 0

print("==========================================")
print("=                               RESULTADOS:                                 =")
print(f"Área total del elipse: {areaElipse:.2f}")
print(f"Puntos totales generados: {cantidad}")
print(f"Puntos que cayeron en el elipse: {puntosElipse}")
print(f"Puntos que cayeron en la intersección: {puntosIntersec}")
print(f"Área aproximada de la intersección: {areaIntersec:.2f}")
print("==========================================")

