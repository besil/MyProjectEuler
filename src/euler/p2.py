'''
Created on Feb 28, 2015

@author: besil
'''

if __name__ == '__main__':
    def fib(n, keep=lambda x:True):
        a = 1
        b = 2
        if keep(a): yield a
        if keep(b): yield b
        curr = a+b
        while curr < n:
            if keep(curr): yield curr
            a = b
            b = curr
            curr = a+b
    
    n = 4000000
    res = lambda n : sum([ x for x in fib(n, keep=lambda x: x%2==0) ])
    print( res(n) )
        
        
        