import math

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
    
