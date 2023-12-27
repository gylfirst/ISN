from math import factorial as fact, ceil
def pas(n) :
    p = ceil(n/2)
    return int(fact(n)/(fact(p)*fact(n-p)))
