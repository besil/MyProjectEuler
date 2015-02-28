'''
Created on Feb 28, 2015

@author: besil
'''

if __name__ == '__main__':
    def sumsquare(l):
        return sum( [ i**2 for i in l ] )
    def squaresum(l):
        return sum(l) ** 2
    
    l = [ x for x in range(1, 101) ]
    
    smsq = sumsquare(l)
    sqsm = squaresum(l)

    print( sqsm - smsq )