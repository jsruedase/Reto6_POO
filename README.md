# Reto6_POO

# Archivos del reto 1:

``` python
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
    try:
        num_elementos = int(input("Ingrese el numero de elementos de la lista: "))
    except:
        num_elementos = 0
        print("Ingrese un número entero")
        
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
```
La primera excepción atrapa el error ValueError: invalid literal for int() with base 10, por no inresar un entero sino un string. Se incluye la excepción a la hora de seleccionar el primer elemento de la lista que se retorna, ya que si el número de elementos es 0, no se puede acceder a ese índice. Por eso en el except, se imprime que diga un número mayor a 0

``` python
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


```
Se crea la excepción de ValueError, cuando se trata de ingresar un valor que no sea un número entero, tanto a la hora de dar el número de elementos, como cuando se eligen los números que componen la lista.

``` python
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


```
Se añade la excepción para evitar el error de ValueError cuando se itnenta ingresar un número que no es un entero, al momento de decir el número de elementos de la lista, tanto en el ciclo para determinar el número a añadir de la lista 

``` python
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


```
Para este programa se hacen dos excepciones, una cuando se intente dividir por 0 y otra para cuando se intente escoger un string en vez de un float a la hora de ingresar num1 y num2. 

``` python
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
```
En este caso, no es necesario el uso de excepciones, ni para el caso que se ingrese la cadena vacía, "", para evaluarla.

# Shape Package

``` python
class Point():
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Las coordenadas deben ser números.")
        self._x = x
        self._y = y
        
    def distance(self, point):
        return math.sqrt((self._x - point.get_x())**2 + (self._y - point.get_y())**2)
    
    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
    
    def get_x(self):    
        return self._x
    
    def get_y(self):    
        return self._y

```
Se comprueba en la excepcion que sean números las coordenadas

``` python
class Line:
    def __init__(self, start, end) -> None:
        self._start = start
        self._end = end
        self._length = self.compute_length()
        self._slope = self.compute_slope()

    def compute_length(self):
        length = math.sqrt((self._start.get_x() - self._end.get_x())**2 + (self._start.get_y() - self._end.get_y())**2)
        return round(length,2)
    
    def compute_slope(self):
        """
        La excepción ZeroDivisionError se lanza cuando la pendiente de la recta es infinita.
        """
        try:
            m = (self._end.get_y() - self._start.get_y()) / (self._end.get_x() - self._start.get_x())
            return round(m,2)
        except ZeroDivisionError:
            return float("inf")
        
    def compute_horizontal_cross(self):
        pos_x_coordinate = (self._slope * self._start.get_x() - self._start.get_y()) / self._slope

        if pos_x_coordinate >= self._start.get_x() and pos_x_coordinate <= self._end.get_x():
            return True
        else:
            return False
        
    def compute_vertical_cross(self):
        pos_y_coordinate = self._start.get_y() - (self._slope * self._start.get_x())

        if pos_y_coordinate >= self._start.get_y() and pos_y_coordinate <= self._end.get_y():
            return True
        else:
            return False
    
    def discretize_line(self, number_of_sections):
        """
        La excepción ValueError se lanza cuando el número de secciones no es un número mayor a 0.
        """
        array_of_points = []
        if number_of_sections <= 0 or not isinstance(number_of_sections, (int, float)):
            raise ValueError("El número de secciones debe ser un número mayor a 0.")
        distance_points = self._length / number_of_sections
        
        if self._slope == float("inf"):
            for i in range(number_of_sections):
                array_of_points.append(Point(self._start.get_x(), self._start.get_y() + i * distance_points))
        elif self._slope == 0:
            for i in range(number_of_sections):
                array_of_points.append(Point(self._start.get_x() + i * distance_points, self._start.get_y()))
        else:
            for i in range(number_of_sections):
                array_of_points.append(Point(self._start.get_x() + i * distance_points, self._start.get_y() + self._slope * i * distance_points))
        
        for point in array_of_points:
            print(f"({point.get_x()}, {point.get_y()})")
    
    def get_start(self):
        return self._start

    def get_end(self):
        return self._end
    
    def get_length(self):
        return self._length
    
    def get_slope(self):
        return self._slope
    
    def set_start(self, start):
        self._start = start
        
    def set_end(self, end):
        self._end = end
        
    def set_length(self, length):
        self._length = length
        
    def set_slope(self, slope):
        self._slope = slope

```
La excepción ZeroDivisionError se lanza cuando la pendiente de la recta es infinita y La excepción ValueError se lanza cuando el número de secciones no es un número mayor a 0 en el metodo de discretizar la recta


``` python
class Shape:
    """
    Entra como parámetro una lista de vértices que forman la figura geométrica, en sentido antihorario. 
    """
    def __init__(self, vertices):
        if len(vertices) < 3:
            raise ValueError("La figura geométrica debe tener al menos 3 vértices.")
        self._vertices = vertices
        self._edges = self.compute_edges()
        self._is_regular = self.check_regular()
        
        
    def compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            if i == len(self._vertices) - 1:
                edges.append(Line(self._vertices[i], self._vertices[0]))
            else:
                edges.append(Line(self._vertices[i], self._vertices[i+1]))
        return edges

    def compute_inner_angles(self):
        inner_angles = []
        for i in range(len(self._vertices)):
            if i == len(self._vertices) - 1:
                angle = math.degrees(math.acos((self._edges[i].get_length()**2 + self._edges[0].get_length()**2 - self._edges[i].get_length()**2) / (2 * self._edges[i].get_length() * self._edges[0].get_length())))
                inner_angles.append(round(angle,1))
            else:
                angle = math.degrees(math.acos((self._edges[i].get_length()**2 + self._edges[i+1].get_length()**2 - self._edges[i].get_length()**2) / (2 * self._edges[i].get_length() * self._edges[i+1].get_length())))
                inner_angles.append(round(angle,1))

        return inner_angles

    def compute_perimeter(self):
        perimeter = 0
        for edge in self._edges:
            perimeter += edge.get_length()
        return perimeter

    def compute_area(self):
        #Fórmula (de Gauss) para calcular el área de un polígono cualquiera
        area = 0
        for i in range(len(self._vertices)):
            if i == len(self._vertices) - 1:
                area += self._vertices[i].get_x() * self._vertices[0].get_y() - self._vertices[0].get_x() * self._vertices[i].get_y()
            else:
                area += self._vertices[i].get_x() * self._vertices[i+1].get_y() - self._vertices[i+1].get_x() * self._vertices[i].get_y()
        return abs(area) / 2

    def check_regular(self):
        if len(set(self.compute_inner_angles())) == 1 and len(set([edge.get_length() for edge in self._edges])) == 1:
            return True
        else:
            return False
```
Acá no se lanzan tantas excepciones ya que partimos que tanto Point como Line sean correctas. Solo se lanza la excepción cuando el númnero de vértices sea menor que 3, no pudiendo formar una forma.

``` python
#Ejemplo de la primera excepción del código: x,y no son números al definir un punto.
try:
    p = Point(1,2)
    print(p.get_x())
except TypeError as e:
    print(e)
    
#Ejemplo de la segunda excepción del código: la pendiente de la recta es infinita.
try:
    l = Line(Point(1,1), Point(1,2))
    print(l.compute_slope())
except ZeroDivisionError as e:
    print(e)

#Ejemplo de la tercera excepción del código: el número de secciones debe ser un entero mayor a 0 al discretizar la línea.
try:
    l = Line(Point(1,1), Point(1,2))
    l.discretize_line(0)
except ValueError as e:
    print(e)
    
#Ejemplo de la cuarta excepción del código: la figura geométrica debe tener al menos 3 vértices al definir una Forma.
try:
    s = Shape([Point(1,1), Point(2,2)])
    print(s.compute_inner_angles())
except ValueError as e:
    print(e)
    
```
Pruebas para ver que las excepciones estén funcionando correctamente
