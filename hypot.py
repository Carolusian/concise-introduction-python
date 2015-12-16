# hypot.py

from math import sqrt

def myhypot(x, y):
    return sqrt(x ** 2 + y ** 2)

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    print("Hypotenuse:", myhypot(a, b))

main()
