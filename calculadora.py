import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de un número negativo"
    return math.sqrt(a)

def logaritmo(a, base=10):
    if a <= 0:
        return "Error: Logaritmo de un número no positivo"
    return math.log(a, base)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tangente")
    print("0. Salir")

while True:
    menu()
    opcion = input("Ingrese su opción: ")

    if opcion == '0':
        break

    if opcion in ['1', '2', '3', '4', '5']:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(a, b))
    elif opcion == '2':
        print("Resultado:", resta(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicacion(a, b))
    elif opcion == '4':
        print("Resultado:", division(a, b))
    elif opcion == '5':
        print("Resultado:", potencia(a, b))
    elif opcion == '6':
        a = float(input("Ingrese el número: "))
        print("Resultado:", raiz_cuadrada(a))
    elif opcion == '7':
        a = float(input("Ingrese el número: "))
        base = float(input("Ingrese la base del logaritmo (default 10): ") or 10)
        print("Resultado:", logaritmo(a, base))
    elif opcion == '8':
        a = float(input("Ingrese el ángulo en grados: "))
        print("Resultado:", seno(a))
    elif opcion == '9':
        a = float(input("Ingrese el ángulo en grados: "))
        print("Resultado:", coseno(a))
    elif opcion == '10':
        a = float(input("Ingrese el ángulo en grados: "))
        print("Resultado:", tangente(a))
    else:
        print("Opción no válida. Intente de nuevo.")