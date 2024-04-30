def conversion_temperaturas(temperatura_celsius):
  """
  Función para convertir una temperatura en Celsius a Fahrenheit y Kelvin.

  Parámetros:
    temperatura_celsius: Valor de temperatura en Celsius (float).

  Retorno:
    Un diccionario con las temperaturas convertidas a Fahrenheit y Kelvin.
  """
  
  # Conversión a Fahrenheit
  temperatura_fahrenheit = (temperatura_celsius * 9.0 / 5.0) + 32.0

  # Conversión a Kelvin
  temperatura_kelvin = temperatura_celsius + 273.15

  # Se retorna un diccionario con las temperaturas convertidas
  temperaturas_convertidas = {
    "Fahrenheit": temperatura_fahrenheit,
    "Kelvin": temperatura_kelvin
  }

  return temperaturas_convertidas

# Ejemplo de uso
temperatura_celsius = 20.0  # Valor de temperatura en Celsius

temperaturas_convertidas = conversion_temperaturas(temperatura_celsius)

print("Temperatura en Fahrenheit:", temperaturas_convertidas["Fahrenheit"])
print("Temperatura en Kelvin:", temperaturas_convertidas["Kelvin"])
