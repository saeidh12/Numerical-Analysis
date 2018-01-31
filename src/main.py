import numpy as np
from algorithms.SecantMethod import SecantMethod
from algorithms.BisectionMethod import BisectionMethod
from algorithms.SecantBisectionHybridMethod import SecantBisectionHybridMethod

def func(x):
    return -1 * np.power(x, 4) + 3 * np.power(x, 2) + 2

def compare(f, epsilon, max_itteration):
    print("%-25s %-20s %-20s %-10s" %('method', 'x', 'f(x)', 'itterations'))
    print("%-25s %-20s %-20s %-10s" %('method', 'x', 'f(x)', 'itterations'), file=open("output.txt", "a"))

    method         = SecantMethod(f, epsilon, max_itteration)
    method_name    = method.name
    x              = method.find(0.0, 3.0)
    fx             = f(x)
    ittr           = method.itterations
    print("%-25s %-20s %-20s %-10s" %(method_name, x, fx, ittr))
    print("%-25s %-20s %-20s %-10s" %(method_name, x, fx, ittr), file=open("output.txt", "a"))

    method         = BisectionMethod(f, epsilon, max_itteration)
    method_name    = method.name
    x              = method.find(0.0, 3.0)
    fx             = f(x)
    ittr           = method.itterations
    print("%-25s %-20s %-20s %-10s" %(method_name, x, fx, ittr))
    print("%-25s %-20s %-20s %-10s" %(method_name, x, fx, ittr), file=open("output.txt", "a"))

    method         = SecantBisectionHybridMethod(f, epsilon, max_itteration)
    method_name    = method.name
    x              = method.find(0.0, 3.0, 0.0)
    fx             = f(x)
    ittr           = method.itterations
    print("%-25s %-20s %-20s %-10s" %(method_name, x, fx, ittr))
    print("%-25s %-20s %-20s %-10s" %(method_name, x, fx, ittr), file=open("output.txt", "a"))

if __name__ == '__main__':
    compare(func, 1 / np.power(10.0, 6), 50)
