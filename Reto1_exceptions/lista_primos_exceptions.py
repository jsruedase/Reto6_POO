"""
    Explicación: Primero necesitamos crear una función que compruebe si un número n es primo o no. Esto es, si no es divisible por ninguno de los numeros anteriores a este, desde el 2 hasta n-1. Luego 
    la funcion filtrar_primos toma la lista que le pasa por parámetro y llama esta función de comprobación con cada número de la lista y si es primo, lo añade a otra nueva lista. FInalmente en el main 
    se llama la función después de haber creado la lista con los datos del usuario.
"""

def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filtrar_primos(lista_num):
    nueva_lista = []
    for num in lista_num:
        if es_primo(num):
            nueva_lista.append(num)
    return nueva_lista

if __name__ == "__main__":
    lista = []
    try:
        num_elementos = int(input("Ingrese el numero de elementos de la lista: "))
        i = 0
        while i < num_elementos:
            num = int(input("Ingrese el numero a añadir a la lista: "))
            lista.append(num)
            i+=1
        lista_filtrada = filtrar_primos(lista)
        print(lista_filtrada)
    except:
        print("Ingrese un número entero")

# Se crea la excepción de ValueError, cuando se trata de ingresar un valor que no sea un número entero, 
# tanto a la hora de dar el número de elementos, como cuando se eligen los números que componen la lista.
