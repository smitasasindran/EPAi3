### **Closures**


#### Assignment Question 1:
Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests)

```
def find_docstring(fn):
```
This function takes an input function, and returns True if the docstring of the function is greater than 50 chars, False otherwise

#### Assignment Question 2:
Write a closure that gives you the next Fibonacci number (+ 2 tests)

```
def get_fibonacci():
```
This function returns the next Fibonacci number in the series, everytime it is called. The series starts from 0


#### Assignment Question 3:
We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) 
```
def count_function(fn):
```
This function keeps track of the number of times the given input function is called.
A global dictionary containing all function names counted to date is also maintained


#### Assignment Question 4:
Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests)

```
def count_function_with_dict(fn, fn_count):
```
This function keeps track of the number of times the given input function is called, just like the above one.
However it allows passing a dictionary which will be updated with the counts. Any existing counts in the dictionary will be added to the running count for the function

