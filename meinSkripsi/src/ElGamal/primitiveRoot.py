'''
Created on Sep 27, 2016

@author: win3a1
'''


factors=[]

def primeFactor(N):
    i=2
    while i*i <=N:
        if pow(N,1,i):
            i+=1
        else:
            N //=1
            factors.append(i)
            print i
    if N>1:
        factors.append(N)
        print N

def primeRoot(m, p):
    None