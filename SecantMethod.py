import numpy as np

class SecantMethod:
    def __init__(self, f, e, max_itterations):
        self.name              = 'Secant'
        self.f                 = f
        self.epsilon           = e
        self.itterations       = 0
        self.max_itterations   = max_itterations

    def method(self, xn_2, xn_1):
        return ( xn_2 * self.f(xn_1) - xn_1 * self.f(xn_2) ) / ( self.f(xn_1) - self.f(xn_2) )

    def find(self, x1, x2):
        if np.absolute(self.f(x2)) < self.epsilon or self.itterations == self.max_itterations:
            return x2
        if np.absolute(self.f(x1)) < self.epsilon:
            return x1
        self.itterations += 1
        return self.find(x2, self.method(x1, x2))

