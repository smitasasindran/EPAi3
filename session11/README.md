### Assignment 11: Iterators and Iterables

Submitted by:   
Smita Sasindran (smitasasindran@gmail.com)

### Assignment  
The starting point for this project is the Polygon class 
and the Polygons sequence type we created in the previous assignment.   

This assignment takes the PolygonSequencer class and creates an iterable

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
and a common circumradius, and returns a Polygon from a precomputed sequence of 'n' regular strictly convex polygons 
(ie polygons with vertices from 3 to 'n', with a common circumradius)

This implementation is split into an iterator and an iterable, where the iterator is defined within the iterable class.  
The PolygonSequencer defines an iterable, which returns a new iterator of type PolygonIterator

The PolygonSequencer implements the following required functions for an iterable:
```
__iter__
```  
On calling the iter function, this class always returns a new iterator of type PolygonIterator. 
In this manner, the iterable is never exhausted, and can be iterated upon as many times as required.  
It also uses a lru cache, so that we create the polygon object only once at class level, which is then used by the Iterator  

The PolygonIterator implements the following required functions:
```
__iter__
__next__
```  
The iter function of an iterator class always returns itself. The next function returns the next polygon from the pre-computed polygon sequence available at the iterable class level

It is defined in polygon_sequencer.py



Link to colab notebook: https://colab.research.google.com/drive/1hXy1UxDayGjVshhBTTzmY04dRgnGQKVA?usp=sharing

Github actions: 
https://github.com/smitasasindran/EPAi3/runs/3153331214?check_suite_focus=true

