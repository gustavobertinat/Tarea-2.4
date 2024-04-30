def es_multiplo(numero, divisor):
  """
  Función para verificar si un número es múltiplo de otro.

  Parámetros:
    numero: El número que se quiere verificar.
    divisor: El divisor a considerar.

  Retorno:
    True si el número es múltiplo del divisor, False en caso contrario.
  """
  return numero % divisor == 0

def main():
  """
  Función principal para verificar si un número es múltiplo de varios números.
  """
  numero = int(input("Ingrese un número: "))

  divisores = [2, 3, 5, 7, 9, 10, 11]

  for divisor in divisores:
    if es_multiplo(numero, divisor):
      print(f"{numero} es múltiplo de {divisor}")
    else:
      print(f"{numero} no es múltiplo de {divisor}")

if __name__ == "__main__":
  main()
