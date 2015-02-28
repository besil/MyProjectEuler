'''
Created on Feb 28, 2015

@author: besil
'''

if __name__ == '__main__':
    def ispitagorean(a,b,c):
        return a**2 + b**2 == c**2
    
    def gen(k):
        for b in range(1, k):
            for c in range(1, k):
                a = k * (k - 2*c) // (2*b)
                if a > 0 and ispitagorean(a, b, c):
                    yield a,b,c
    
    n = 1000
    for a,b,c in gen(n):
        print("{} * {} * {} = {}".format(a,b,c, a*b*c) )