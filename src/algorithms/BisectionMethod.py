import numpy as np

class BisectionMethod:
    def __init__(self, f, e, max_itterations):
        self.name              = 'Bisection'
        self.f                 = f
        self.epsilon           = e
        self.itterations       = 0
        self.max_itterations   = max_itterations

    def method(self, a, b):
        return (a + b) / 2

    def find(self, a, b):
        if np.absolute(self.f(a)) < self.epsilon or self.itterations == self.max_itterations:
            return a
        if np.absolute(self.f(b)) < self.epsilon:
            return b
        
        self.itterations += 1

        c = self.method(a, b)

        if self.f(a) * self.f(c) < 0:
            return self.find(a, c)
        elif self.f(c) * self.f(b) < 0:
            return self.find(c, b)
        else:
            return "wrong input; f(a) * f(b) must be negative"
