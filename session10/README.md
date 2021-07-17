### Assignment 10: Sequences

Submitted by:   
Smita Sasindran (smitasasindran@gmail.com)



### Q1: Polygon class 
A regular strictly convex polygon is a polygon that has the following characteristics:
 - all interior angles are less than 180
 - all sides have equal length
    
This class represents a regular strictly convex polygon of 'n' vertices, and circumradius 'r'. n should be >2
The following properties are available, which are calculated based on # of vertices and the circumradius:
```
interior_angle
edge_length
apothem
area
perimeter
```
It also implements an equality check, and a greater than check (depending only on the # of vertices)   
It is defined in polygon.py 


### Q2: Custom Polygon sequence
This class implements a custom sequence of type Polygon. 
It takes as input the max number of vertices and a common circumradius, to define a sequence of 'n' regular strictly convex polygons (ie polygons with vertices from 3 to 'n', with a common circumradius)
It implements the following requried functions for a custom sequence:
```
__getitem__
__len__
```
It also uses a lru cache, so that we create the polygon object only once
It is defined in custom_polygon.py


