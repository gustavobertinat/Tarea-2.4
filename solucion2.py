# Se inicializan las variables
calificacion1 = 0
calificacion2 = 0
calificacion3 = 0
calificacion4 = 0
calificacion5 = 0
promedio = 0

# Se solicitan las calificaciones al usuario
print("Ingrese la primera calificación:")
calificacion1 = float(input())

print("Ingrese la segunda calificación:")
calificacion2 = float(input())

print("Ingrese la tercera calificación:")
calificacion3 = float(input())

print("Ingrese la cuarta calificación:")
calificacion4 = float(input())

print("Ingrese la quinta calificación:")
calificacion5 = float(input())

# Se calcula el promedio
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

# Se muestra el promedio al usuario
print("El promedio de las calificaciones es:", promedio)
