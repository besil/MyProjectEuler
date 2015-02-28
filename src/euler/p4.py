'''
Created on Feb 28, 2015

@author: besil
'''

def ispal(s):
    s = str(s)
    return s == s[::-1]

if __name__ == '__main__':
    
    def answer(lb, ub):
        return max( [ i*j for i in range(lb, ub) for j in range(lb, ub) if ispal(i*j) ] )
    
    print( answer(100, 999) )