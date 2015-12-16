# montecarlomp.py
# Revised 17 Jun 2013 to add tries

from random import uniform
from math import exp
import multiprocessing

def count_hits(f, a, b, m, n):
    hits = 0
    for i in range(n):
        x = uniform(a, b)
        y = uniform(0, m)
        if y <= f(x):
            hits += 1
    return hits

def estimate_area_mp(f, a, b, m, n=1000):
    workers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(workers)
    total = m * (b - a)
    x = [a + i * (b - a) / workers for i in range(workers + 1)]
    hits = []
    tries = [n // workers] * workers
    tries[workers - 1] = n - (workers - 1) * (n // workers)
    for i in range(workers):
        pool.apply_async(count_hits,
                         (f, x[i], x[i + 1], m, tries[i]),
                         callback=hits.append)
    pool.close()
    pool.join()
    return sum(hits) * total / n

def f(x):
    return exp(-x ** 2)

def main():
    print(estimate_area_mp(f, 0, 2, 1, 1000000))

if __name__ == "__main__":
    main()
