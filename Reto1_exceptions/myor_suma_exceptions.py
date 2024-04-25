def mayor_suma_dos_consecutivos(lista):
    """
    Explicación: Primero, se inicializa una variable que va a guardar la mayor suma con valor de menos infinito, para que así, cualquier suma encontrada sea mayor que ese valor inicial. Luego se va
    recorriendo la lista por las posiciones y se hace la suma del i-ésimo con el siguiente y se compara con la mayor suma. Si esta suma es mayor a mayor_suma, entonces la mayor suma será la suma del ciclo
    Cuando haya recorrido todos los elementos, retorna la mayor.
    
    """
    mayor_suma = float("-inf")
    for i in range(0, len(lista)-1):
        suma = lista[i] + lista[i+1]
        if suma > mayor_suma:
            mayor_suma = suma
    return mayor_suma



if __name__ == "__main__":
    lista = []
    try:
        num_elementos = int(input("Ingrese el numero de elementos de la lista (>=2): "))
        i = 0
        while i < num_elementos:
            num = int(input("Ingrese el numero a añadir a la lista: "))
            lista.append(num)
            i+=1
        mayor_suma = mayor_suma_dos_consecutivos(lista)
        print(mayor_suma)
    except:
        print("Ingrese un número entero")

# Se añade la excepción para evitar el error de ValueError cuando se itnenta ingresar un número que no es un entero,
# al momento de decir el número de elementos de la lista, tanto en el ciclo para determinar el número a añadir de la lista 
