import pytest
import math

from polygon import Polygon
from polygon_sequencer import Polygons


# Test cases from class
def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass

    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

    assert math.isclose(p.side_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.side_length},'
                                           f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


# =================================
# Testing that old functions from Assignment 11 are still working as before


def test_polygon_iteratble():
    # Test that PolygonSequencer is an iterable that can be iterated upon multiple times
    polygons = Polygons(5, 7)

    assert len(polygons) == polygons.n

    # Test that we get same count of sequence on iterating multiple times
    loop1_index = 0
    loop1_p1 = None
    for p in polygons:
        loop1_index += 1
        if loop1_index == 1:
            loop1_p1 = p

    # Loop 2
    loop2_index = 0
    loop2_p1 = None
    poly_iter = iter(polygons)
    while True:
        try:
            p = next(poly_iter)
            loop2_index += 1
            if loop2_index == 1:
                loop2_p1 = p
        except StopIteration as ex:
            break

    # Loop 3
    loop3_index = 0
    loop3_p1 = None
    for p in polygons:
        loop3_index += 1
        if loop3_index == 1:
            loop3_p1 = p

    assert loop1_index == polygons.n
    assert loop2_index == loop1_index
    assert loop3_index == loop1_index

    print("Loop1 p1: ", loop1_p1)
    print("Loop2 p1: ", loop2_p1)
    print("Loop3 p1: ", loop3_p1)
    assert loop1_p1 == loop2_p1
    assert loop2_p1 == loop3_p1
    print("End of test 1\n\n")



