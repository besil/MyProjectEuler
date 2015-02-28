'''
Created on Feb 28, 2015

@author: besil
'''

if __name__ == '__main__':
    def primeGen(limit):
        primes = []
        n = 2
        
        def isprime(m):
            for p in primes: 
                if m % p == 0: return False
            return True
        
        count = 0
        while count < limit:
            if isprime(n):
                count += 1
                primes.append(n)
                yield n
            n += 1
        
    for p in primeGen(10001):
        print(p)