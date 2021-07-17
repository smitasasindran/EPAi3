import pytest

from polygon import Polygon
from custom_polygon import CustomPolygonSequencer


def test_polygon_angle():
    polygon = Polygon(5, 7)
    interior_angle = polygon.calc_interior_angle()
    assert interior_angle == 171.88733853924697

def test_polygon_edge_length():
    polygon = Polygon(3, 7)
    edge_length = polygon.calc_edge_length()
    assert edge_length == 12.12435565298214

def test_polygon_apothem():
    polygon = Polygon(3, 7)
    apothem = polygon.calc_apothem()
    assert apothem == 3.500000000000001

def test_polygon_area():
    polygon = Polygon(4, 2)
    area = polygon.calc_area()
    assert area == 8.0

def test_polygon_perimeter():
    polygon = Polygon(4, 2)
    perimeter = polygon.calc_perimeter()
    assert perimeter == 11.31370849898476

def test_polygon_properties():
    polygon = Polygon(5, 7)
    assert polygon.interior_angle == 171.88733853924697
    assert polygon.edge_length == 8.228993532094623
    assert polygon.apothem == 5.663118960624632
    assert polygon.area == 116.5044232461563
    assert polygon.perimeter == 41.144967660473114

def test_polygon_repr():
    polygon = Polygon(5, 7)
    assert str(polygon) == "Polygon(Vertices: 5, CircumRadius: 7)"

def test_polygon_eq():
    p1 = Polygon(3, 5)
    p2 = Polygon(3, 5)
    p3 = Polygon(3, 7)
    p4 = Polygon(4, 5)

    assert (p1 == p2) == True
    assert (p1 != p3) == True
    assert (p1 != p4) == True

def test_polygon_gt():
    p1 = Polygon(3, 5)
    p2 = Polygon(3, 5)
    p3 = Polygon(4, 5)
    p4 = Polygon(3, 7)

    assert (p1 > p2) == False
    assert (p1 > p3) == False
    assert (p3 > p1) == True
    assert (p1 > p4) == False
    assert (p4 > p1) == False

def test_polygon_seq():
    custom1 = CustomPolygonSequencer(5, 7)
    print("Test 1 Custom Polygon sequence: ", list(custom1))
    p1 = custom1[0]
    p2 = custom1[1]
    p3 = custom1[2]
    assert p1.no_of_vertices == 3
    assert p1.circumradius == 7

    assert p3.no_of_vertices == 5
    assert p3.circumradius == 7

def test_polygon_seq_max_efficiency():
    custom1 = CustomPolygonSequencer(5, 7)
    print("Test 2 Custom Polygon sequence: ", list(custom1))

    max_ratio, index = custom1.max_efficiency_polygon()
    pmax = custom1[index]

    assert max_ratio == 2.831559480312316
    assert index == 5 - 3
    assert pmax.no_of_vertices == 5

