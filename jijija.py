def calculator():
    num1 = float(input("Ingresa el primer número: "))
    operation = input("Ingresa la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: división por cero"
    else:
        result = "Operación no válida"

    print(f"El resultado es: {result}")

calculator() 

