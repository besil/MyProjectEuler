'''
Created on Feb 28, 2015

@author: besil
'''
import unittest
import math

class P3:
    def answer(self, n):
        def reduce(n, p):
            while n % p == 0:
                n = n / p
            return n
        
        for p in self.primeGen(limit=int(math.sqrt(n))):
            n = reduce(n, p)
            if n == 1:
                return p
    
    def factors(self, n):
        t = int( math.sqrt(n) )
        res = [ x for x in self.primeGen(limit=t) if n % x == 0 ]
        return res
    
    def primeGen(self, limit=None):
        primes = []
        n = 2
        
        def isprime(m):
            for p in primes: 
                if m % p == 0: return False
            return True
        
        top = lambda t : (t < limit) if limit is not None else True
        while top(n):
            if isprime(n):
                primes.append(n)
                yield n
            n += 1

class TestProblem3(unittest.TestCase):
    
    def setUp(self):
        self.p3 = P3()
    
    def test_factors(self):
        self.assertEqual([5, 7, 13, 29], self.p3.factors(13195) )
    
if __name__ == '__main__':
    p3 = P3()
    n = 600851475143
    print( p3.answer(n) )
    
    unittest.main()