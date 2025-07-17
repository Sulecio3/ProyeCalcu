print("Bienvenido al programa de Calculadora")
opcion = ""

while opcion != "5":
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a + b)

    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a - b)

    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a * b)

    elif opcion == "4":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        if b == 0:
            print("¡Error! No se puede dividir entre 0.")
        else:
            print("Resultado:", a / b)

    elif opcion == "5":
        print("¡Adiós!")

    else:
        print("Opción inválida. Intenta de nuevo.")