import numpy as np
from .BisectionMethod import BisectionMethod as BM
from .SecantMethod import SecantMethod    as SM

class SecantBisectionHybridMethod:
    def __init__(self, f, e, max_itterations):
        self.name              = 'Secant Bisection Hybrid'
        self.f                 = f
        self.epsilon           = e
        self.itterations       = 0
        self.max_itterations   = max_itterations
        self.secant            = SM(f, e, max_itterations)
        self.bisection         = BM(f, e, max_itterations)

    def method(self, ak, bk, bk_1):
        s = self.secant.method(bk_1, bk)
        m = self.bisection.method(ak, bk)

        if s > m and s < bk:
            return s
        else:
            return m

    def find(self, ak, bk, bk_1):
        if np.absolute(self.f(ak)) < np.absolute(self.f(bk)):
            ak, bk = bk, ak
            bk_1 = ak

        if np.absolute(self.f(bk)) < self.epsilon or self.itterations == self.max_itterations:
            return bk

        self.itterations += 1

        bk1 = self.method(ak, bk, bk_1)

        if self.f(ak) * self.f(bk1) > 0:
            ak = bk

        return self.find(ak, bk1, bk)
