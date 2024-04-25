def operaciones_basicas(num1, num2, operacion):
    """
    Explicación: Primero se crea el main y se pide al usuario que ingrese los dos numeros, que pueden ser decimales, y la operación. Si la operación que se ingresa no está
    dentro de las opciones, retorna un string donde dice que elija la opción correcta.
    """
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1-num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        try:
            return num1 / num2
        except:
            return "No se puede dividir por 0"
    else:
        return "Elija una operación correcta"
    
if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese un primer número: "))
        num2 = float(input("Ingrese un segundo número: "))
        operacion = input("Ingrese una operación (+, -, *, /): ")
        resultado = operaciones_basicas(num1, num2, operacion)
        print(resultado)
    except:
        print("Escoja un número válido")

# Para este programa se hacen dos excepciones, una cuando se intente dividir por 0 y otra para cuando se intente escoger
# un string en vez de un float a la hora de ingresar num1 y num2. 
