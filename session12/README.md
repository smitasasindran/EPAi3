### Assignment 12: Iterators and Iterables II

Submitted by:   
Smita Sasindran (smitasasindran@gmail.com)

### Assignment  
The starting point for this project is the Polygon class 
and the Polygons sequence type we created in the previous assignment.   

#### Goal 1: 
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

#### Goal 2: 
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.    
You'll need to implement both an iterable, and an iterator.   


### Polygon class 
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

### Custom Polygon iterable
This class creates an iterable which returns Polygon class objects.  It takes as input the max number of vertices 
and a common circumradius, and computes and returns the next Polygon in the expected sequence of 'n' regular strictly convex polygons 
(ie polygons with vertices from 3 to 'n', with a common circumradius)   
Since the requirement is for lazy computation and to not store precomputed objects, the next Polygon object is generated everytime 


This implementation is split into an iterator and an iterable, where the iterator is defined within the iterable class.  
The Polygons defines an iterable, which returns a new iterator of type PolygonIterator

The Polygons class implements the following required functions for an iterable:
```
__iter__
```  
On calling the iter function, this class always returns a new iterator of type PolygonIterator. 
In this manner, the iterable is never exhausted, and can be iterated upon as many times as required. 

The PolygonIterator implements the following required functions:
```
__iter__
__next__
```  
The iter function of an iterator class always returns itself. The next function computes and returns the next polygon

It is defined in polygon_sequencer.py


Link to colab notebook: https://colab.research.google.com/drive/1WEJ2x8hWT1Y63DwC2BAZ6vvmv3hoetoT?usp=sharing

Github actions: 
https://github.com/smitasasindran/EPAi3/runs/3153331214?check_suite_focus=true

