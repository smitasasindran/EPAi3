from functools import lru_cache
from polygon import Polygon

class CustomPolygonSequencer:
    """
    This class takes in the max number of vertices, and a common circumradius, to define a
    sequence of 'n' regular strictly convex polygons
    """

    def __init__(self, n, r):
        if n <= 2:
            raise ValueError('Number of vertices for polygon sequence cannot be less than 3')

        self.n = n - 2
        self.circumradius = r

    def max_efficiency_polygon(self):
        polygons = [CustomPolygonSequencer._polygon(i, self.circumradius) for i in range(0, self.n)]
        # print("Polygons are: ", polygons)
        # area_perimeter_ratio = [polygon.area / polygon.perimeter for polygon in polygons]
        # print(area_perimeter_ratio)

        area_perimeter_ratio = [(polygon.area / polygon.perimeter, i) for i, polygon in enumerate(polygons)]
        print(area_perimeter_ratio)
        print("Max is: ", max(area_perimeter_ratio))

        return max(area_perimeter_ratio)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        print("\nIn getitem: index=", index)
        if isinstance(index, int):
            if index < 0 or index > self.n-1:
                raise IndexError
            else:
                return CustomPolygonSequencer._polygon(index, self.circumradius)
        else:
            start, stop, step = index.indices(self.n)
            rng = range(start, stop, step)
            return [CustomPolygonSequencer._polygon(i, self.circumradius) for i in rng]

    @staticmethod
    @lru_cache(2 ** 5)
    def _polygon(n, r):
        # Polygon sequence starts from 3. ie polygon at position 0 will have 3 sides, ... etc
        polygon = Polygon(n + 3, r)
        print(f"Polygon for index {n} is {polygon}")
        return polygon