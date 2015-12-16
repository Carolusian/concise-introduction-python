# primes.py

def isprime(n):
    # Return True if n is prime.
    return n > 1 and smallestdivisor(n) == n

def smallestdivisor(n):
    # Find smallest divisor (other than 1) of integer n > 1.
    k = 2
    while k < n and not divides(k, n):
        k += 1
    return k

def divides(k, n):
    # Return True if k divides n.
    return n % k == 0

def main():
    for n in range(2, 100):
        if isprime(n):
            print(n, end=" ")
    print()
        
main()
