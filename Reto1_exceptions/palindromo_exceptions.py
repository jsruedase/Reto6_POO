def es_palindromo(palabra):
    """
    Explicación: Se comprueba la primera posición del string con la última, la segunda con la penúltima y así sucesivamente. En el caso de que no coincida alguna de estas, la palabra no es palindroma 
    y retorna False la función.
    """
    lo_es = True
    for i in range(0, len(palabra)-1):
        if palabra[i] != palabra[len(palabra)-1-i]:
            lo_es = False
    return lo_es

if __name__ == "__main__":
    palabra = input("Ingrese la palabra a verificar: ")
    if es_palindromo(palabra):
        print("La palabra es palíndroma")
    else:
        print("La palabra no es palíndroma")

# En este caso, no es necesario el uso de excepciones, ni para el caso que se ingrese la cadena vacía, "", para evaluarla.
