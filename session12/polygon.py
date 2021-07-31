import math

class Polygon:
    """
    This class represents a regular strictly convex polygon of 'n' vertices, and circumradius 'r'
    """

    def __init__(self, n, r):
        if n <= 2:
            raise ValueError('Number of vertices of polygon cannot be less than 3')

        self._n = n
        self._R = r

        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        self._efficiency = None

    def calc_interior_angle(self):
        angle = (self._n - 2) * 180 / self._n
        return angle

    def calc_side_length(self):
        s = 2 * self._R * math.sin(math.pi / self._n)
        return s

    def calc_apothem(self):
        a = self._R * math.cos(math.pi / self._n)
        return a

    def calc_area(self):
        area = 0.5 * self._n * self.side_length * self.apothem
        return area

    def calc_perimeter(self):
        perimeter = self._n * self.side_length
        return perimeter

    def calc_efficiency(self):
        efficiency = self.area / self.perimeter
        return efficiency

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        if not self._interior_angle:
            self._interior_angle = self.calc_interior_angle()
        return self._interior_angle

    @property
    def side_length(self):
        if not self._side_length:
            self._side_length = self.calc_side_length()
        return self._side_length

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

    @property
    def efficiency(self):
        if not self._efficiency:
            self._efficiency = self.calc_efficiency()
        return self._efficiency

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    def __gt__(self, polygon2):
        return self.count_edges > polygon2.count_edges

    def __eq__(self, polygon2):
        return self.count_edges == polygon2.count_edges and self.circumradius == polygon2.circumradius

