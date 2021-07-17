import math

class Polygon:
    """
    This class represents a regular strictly convex polygon of 'n' vertices, and circumradius 'r'
    """

    def __init__(self, n, r):
        if n <= 2:
            raise ValueError('Number of vertices of polygon cannot be less than 3')

        self.no_of_vertices = n
        self.circumradius = r

        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    def calc_interior_angle(self):
        angle = (self.no_of_vertices - 2) * 180 / math.pi
        return angle

    def calc_edge_length(self):
        s = 2 * self.circumradius * math.sin(math.pi / self.no_of_vertices)
        return s

    def calc_apothem(self):
        a = self.circumradius * math.cos(math.pi / self.no_of_vertices)
        return a

    def calc_area(self):
        area = 0.5 * self.no_of_vertices * self.edge_length * self.apothem
        return area

    def calc_perimeter(self):
        perimeter = self.no_of_vertices * self.edge_length
        return perimeter

    @property
    def interior_angle(self):
        if not self._interior_angle:
            self._interior_angle = self.calc_interior_angle()
        return self._interior_angle

    @property
    def edge_length(self):
        if not self._edge_length:
            self._edge_length = self.calc_edge_length()
        return self._edge_length

    @property
    def apothem(self):
        if not self._apothem:
            self._apothem = self.calc_apothem()
        return self._apothem

    @property
    def area(self):
        if not self._area:
            self._area = self.calc_area()
        return self._area

    @property
    def perimeter(self):
        if not self._perimeter:
            self._perimeter = self.calc_perimeter()
        return self._perimeter


    def __repr__(self):
        return f'Polygon(Vertices: {self.no_of_vertices}, CircumRadius: {self.circumradius})'

    def __gt__(self, polygon2):
        return self.no_of_vertices > polygon2.no_of_vertices

    def __eq__(self, polygon2):
        return self.no_of_vertices == polygon2.no_of_vertices and self.circumradius == polygon2.circumradius

