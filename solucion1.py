def orden_ascendente(a, b, c):
    if a < b < c:
        return a, b, c
    elif a < c < b:
        return a, c, b
    elif b < a < c:
        return b, a, c
    elif b < c < a:
        return b, c, a
    else:
        return c, a, b

# Ejemplo de uso:
num1 = 5
num2 = 2
num3 = 7

ordenados = orden_ascendente(num1, num2, num3)
print("Números ordenados en forma ascendente:", ordenados)







