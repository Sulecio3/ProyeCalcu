print("Bienvenido al programa de Calculadora")
opcion = ""

while opcion != "5":
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("6. Sorpresa")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Bienvenido a la suma :) ")
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a + b)
        input()

    elif opcion == "2":
        print("Bienvenido a la resta :) ")
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a - b)
        input()

    elif opcion == "3":
        print("Bienvenido a la multiplicacion :)")
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a * b)
        input()

    elif opcion == "4":
        print("Bienvenido a la division :) ")
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        if b == 0:
            print("No se puede dividir entre 0 :(")
            input()
        else:
            print("Resultado:", a / b)
            input()

    elif opcion == "5":
        print("saliendo del programa bay")


    elif opcion == "6":
        print("Hola :)")
        input()

    else:
        print("Opción inválida. Intenta de nuevo :P ")
        input()








