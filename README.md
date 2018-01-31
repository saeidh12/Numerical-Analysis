# Numerical-Analysis
This is my code related to numerical analysis methods and algorithms. You will find the actual methods and algorithms in the algorithms module & an example of thier usage in the main.py file.


### Derivative.py
A class for a function with a method to calculate the direvitive at `x` with O(h^2j).

1. Either pass your desired function in the cunstructor or define a class inheriting from Function and overide it's `function(self, x)` method to be your desired function.

2. Call the `differentiate` to find the derivative of the function at point `x` with O(h^j)
