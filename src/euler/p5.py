'''
Created on Feb 28, 2015

@author: besil
'''
from euler.p3 import P3

if __name__ == '__main__':
    primes = list( P3().primeGen(20) )

    def factorize(n, primes):
        def reduce(n, p):
            c = 0
            while n % p == 0:
                n = n // p
                c+=1
            return n, p, c
        
        d = {}
        for p in primes:
            n, p, c = reduce(n, p)
            if c != 0:
                # print(n, p, c)
                d[p] = c
            if n == 1:
                break
        return d
        
    factors = dict()        
    for i in range(1, 20):
        d = factorize(i, primes)
        for k, v in d.items():
            factors[k] = v if k not in factors else max([factors[k], v])
    
    from functools import reduce
    print( reduce( lambda a, b: a*b, [ k ** v for k, v in factors.items() ] ) )
    
    
