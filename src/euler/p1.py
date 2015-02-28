'''
Created on Feb 28, 2015

@author: besil
'''

if __name__ == '__main__':
    res = lambda n : sum( [ x for x in range(n) if x % 3 == 0 or x % 5 == 0 ] )
    
    print( res(10) )
    print( res(1000) )