"""
Explicación: La función recibe por parámetro una lista de strings, los cuales son analizados en dos ciclos for: el primero coge la palabra, coge las letras de la palabra en
una lista y crea una lista lista_mismas_letras, donde se meterán los anagramas referentes a esa palabra. El segundo ciclo vuelve a iterar la lista original pero compara las 
letras de palabra_2 y si encuentra una letra que no se encuentre en la palbra del primer ciclo, no se añade a la lista de anagramas de esta palabra. En caso de que todas sus 
letras estén, se evalua si la longitud de la palabra sea la misma, sino no son anagramas. Finalmente, por cada palabra se añade a una lista total, la cual no tiene elementos 
repetidos. Como no se especifica en el enunciado, se toma como consideración que se están buscando los anagramas a la palabra en la primera posición de la lista y esa es la 
que se imprime.

"""



def find_anagrams(lista):
    lista_tot = []
    for palabra in lista:
        lista_mismas_letras = []
        list_palabra = list(palabra)
        for palabra_2 in lista:
            añadir = True
            for letra in palabra_2:
                if letra not in list_palabra:
                    añadir = False
                    break
            if añadir and len(palabra_2) == len(palabra):
                lista_mismas_letras.append(palabra_2)
        if lista_mismas_letras not in lista_tot:
            lista_tot.append(lista_mismas_letras) 
    return lista_tot
            

if __name__ == "__main__":
    lista = []
    num_elementos = int(input("Ingrese el numero de elementos de la lista: "))
    i = 0
    while i < num_elementos:
        num = input("Ingrese las palabras a añadir a la lista: ")
        lista.append(num)
        i+=1
    lista_listas = find_anagrams(lista)
    try:
        lista_primer = lista_listas[0]
        print(lista_primer)
    except:
        print("El número de elementos debe ser mayor a 1")

# Se incluye la excepción a la hora de seleccionar el primer elemento de la lista que se retorna, ya que si el número de elementos es 0, no se puede acceder a ese índice. Por eso en el except, se imprime que diga un número mayor a 0

