# Fast-Extremums-Finder
Finds extremums in an equation in sort of a brute-force way.
Using a range (start and end points) and an interval in order to find extremums in the given equation, if there're any.

In order to use the script the function that should be used is the "FindExtremums" function.
An example of a usage:
```python
FindExtremums(CheckEquation("x^2 + 3*x  + 2"), -100, 100, 0.5)
```
Which results in 1 minimum point at (-1.5, -0.25)
