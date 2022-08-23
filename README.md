# Fast-Extremums-Finder
Finds extremums in an equation in sort of a brute-force way (based on a given interval).

Using a range (start and end points) and an interval in order to find extremums in the given equation, if there're any.
<br/><br/>


Doing it this way has its benefits and drawbacks.

Benefits:

  * No need to find the derivative of the equation manually.
  
  * Sometimes it might be too complicated to find the derivative of the equation even for a machine to do it fast enough.
  
  * Sometimes the user knows the range of which the equation is gonna be used at, so only need to test different intervals.
  
Drawbacks:

  * If the extremum isn't in the mentioned range, or that it's but the interval had skipped over it.
  
  * The higher the ratio between the mentioned range to the interval the longer it will take for the script to run.
<br/><br/>

In order to use the script the function that should be used is the "FindExtremums" function.

An example of a usage:

```python
FindExtremums(equations_solver.CheckEquation("x^2 + 3*x  + 2"), -100, 100, 0.5)
```

Which results in 1 minimum point at (-1.5, -0.25), that means that the minimum point's X is above -2 and under -1 (because the interval is 0.5).

Can run it again in that specific range with a smaller interval in order to find a more accurate result.
<br/><br/>


Included the file "requirements_installation.bat" to install the packages from the requirements text file, from this other repo of mine:

https://github.com/xSpecialFoodx/Requirements-Manager
<br/><br/>


Included the file "equations_solver.py" to run the equations at every interval, from this other repo of mine:

https://github.com/xSpecialFoodx/Equations-Solver
