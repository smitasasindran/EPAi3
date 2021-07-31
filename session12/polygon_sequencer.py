from functools import lru_cache
from polygon import Polygon



class Polygons:
    """
    This class takes in the max number of vertices, and a common circumradius, to define a
    sequence of 'n' regular strictly convex polygons.
    This class is an iterable
    """

    def __init__(self, n, r):
        if n <= 2:
            raise ValueError('Number of vertices for polygon sequence cannot be less than 3')

        self.n = n - 2
        self.circumradius = r
        self.polygons = self.get_polygons()
        # print("Polygons are: ", self.polygons)

    def max_efficiency_polygon(self):
        area_perimeter_ratio = [(polygon.efficiency, i) for i, polygon in enumerate(self.polygons)]
        return max(area_perimeter_ratio)

    def get_polygons(self):
        """Function to get the sequence of polygons"""
        p = [Polygons._polygon(i, self.circumradius) for i in range(0, self.n)]
        return p

    def __iter__(self):
        print("Calling Custom Polygons __iter__ function")
        return self.PolygonIterator(self)

    def __len__(self):
        return self.n

    def __repr__(self):
        return f'Polygons(m={self.n}, R={self.circumradius})'

    def __getitem__(self, index):
        # print("\nIn getitem: index=", index)
        if isinstance(index, int):
            if index < 0 or index > self.n-1:
                raise IndexError
            else:
                return Polygons._polygon(index, self.circumradius)
        else:
            start, stop, step = index.indices(self.n)
            rng = range(start, stop, step)
            return [Polygons._polygon(i, self.circumradius) for i in rng]

    @staticmethod
    @lru_cache(2 ** 5)
    def _polygon(n, r):
        # Polygon sequence starts from 3. ie polygon at position 0 will have 3 sides, ... etc
        polygon = Polygon(n + 3, r)
        # print(f"Polygon for index {n} is {polygon}")
        return polygon


    class PolygonIterator:
        def __init__(self, polygon_obj):
            self._index = 0
            self._polygon_obj = polygon_obj

        def __iter__(self):
            print("Calling PolygonIterator __iter__ function")
            return self

        def __next__(self):
            print("Calling PolygonIterator __next__ function: index=", self._index)

            if self._index >= len(self._polygon_obj.polygons):
                raise StopIteration
            else:
                item = self._polygon_obj.polygons[self._index]
                self._index += 1
                return item

