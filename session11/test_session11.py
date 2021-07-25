import pytest

from polygon import Polygon
from polygon_sequencer import PolygonSequencer



def test_polygon_iteratble():
    # Test that PolygonSequencer is an iterable that can be iterated upon multiple times
    polygons = PolygonSequencer(5, 7)

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

# =================================
# Testing that old functions from Assignment 10 are still working as before


def test_polygon_seq():
    polygons = PolygonSequencer(5, 7)
    print("\nTest 2 Custom Polygon sequence: ", list(polygons))
    p1 = polygons[0]
    p2 = polygons[1]
    p3 = polygons[2]
    assert p1.no_of_vertices == 3
    assert p1.circumradius == 7

    assert p3.no_of_vertices == 5
    assert p3.circumradius == 7

    assert len(polygons) == polygons.n
    print("End of test 2\n")

def test_polygon_seq_max_efficiency():
    polygons = PolygonSequencer(5, 7)
    print("\nTest 3 Custom Polygon sequence: ", list(polygons))

    max_ratio, index = polygons.max_efficiency_polygon()
    pmax = polygons[index]

    assert max_ratio == 2.831559480312316
    assert index == 5 - 3
    assert pmax.no_of_vertices == 5

