'''
Created on Feb 28, 2015

@author: besil
'''
import math
def primeGen(limit=None):
    primes = [2]
    n = 3
    
    def isprime(m):
        for p in primes: 
            if m % p == 0: return False
        return True
    
    top = lambda t : (t < limit) if limit is not None else True
    while top(n):
        if isprime(n):
            primes.append(n)
            yield n
        n += 2

def erato(limit):
    crosslimit = int(math.sqrt(limit))
    sieve = [ True for x in range(limit) ]  # @UnusedVariable
    for n in range(4, limit, 2):
        sieve[n] = False
    
    for n in range(3, crosslimit+1, 2):
        if sieve[n]:
            for m in range(n*n, limit, 2*n):
                sieve[m] = False
    
    return sieve
    