# montecarlo.py

from random import uniform
from math import exp

def estimate_area(f, a, b, m, n=1000):
    # Estimate area under f over [a, b] for f positive and <= m.
    hits = 0
    total = m * (b - a)
    for i in range(n):
        x = uniform(a, b)
        y = uniform(0, m)
        if y <= f(x):
            hits += 1
    frac = hits / n
    return frac * total

def f(x):
    return exp(-x ** 2)

def main():
    print(estimate_area(f, 0, 2, 1))
    
main()
