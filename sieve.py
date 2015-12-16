# sieve.py

def sieve(n):
    primes = list(range(2, n + 1))
    for k in range(2, n + 1):
        if k in primes:
            for j in range(2 * k, n + 1, k):
                if j in primes:
                    primes.remove(j)
    return primes

def main():
    n = int(input("Enter upper limit: "))
    print("The primes up to", n, "are:\n", sieve(n))
            
main()
