import numpy as np


class Function():
    def __init__(self, function=None):
        self.Ns = {}
        if function:
            self.f = function
    
    def f(self, x): # overide this function with your desired function
        return x

    def differentiate(j, h, x):
	if (j == 1):
	    return (self.f(x + h) - self.f(x - h))/ (2 * h)

	if (str(j - 1) + "-" + str(h / 2)) not in Ns:
	    Ns[str(j - 1) + "-" + str(h / 2)] = N(j - 1, h / 2, x)

	if (str(j - 1) + "-" + str(h)) not in Ns:
	    Ns[str(j - 1) + "-" + str(h)] = N(j - 1, h, x)
	
	result = Ns[str(j - 1) + "-" + str(h / 2)] + ( ( Ns[str(j - 1) + "-" + str(h / 2)] - Ns[str(j - 1) + "-" + str(h)] ) / ( np.power(4, j - 1) - 1 ) )
	Ns.clear()
	return result

#     def __del__(self):
# 	Ns.clear()
