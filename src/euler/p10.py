'''
Created on Feb 28, 2015

@author: besil
'''
from euler.commons import erato


if __name__ == '__main__':
    limit = 2000000
    sieve = erato(limit)
    
    s = 0
    for n in range(2, limit):
        if sieve[n]:
            s += n
    
    print(s)