'''
Created on Sep 19, 2016

@author: win3a1
'''
from random import randint
import timeit


global k


def pengujianMSR(n):
    msrTimer1 = timeit.default_timer()
    t=1
    k=0
    m = n - 1
    while(m%2==0):
        t=t+1
        m = m/2
    MSRlist =[]
    for k in range(0,20):
        a = randint(2,n-2)
        MSRlist.append(a)
        while(MSRlist.count(a)>0):
            a = randint(2,n-2)
        x = (pow(a,m))%n
        if(t==1 and (x!=1 or x != n-1)): return False
        elif(x==1 or x == n-1):
            continue
        else:
            j=1
            while(j<t-1):
                del x
                x = (pow(2,j))*m
                x = (pow(a,x))%n
                if(x==1):
                    return False
                elif(x==n-1):
                    break
                    continue
                else:
                    j+=1
            del x
            x = (pow(2,(t-1)))*m
            x = (pow(a,x))%n
            if(x==n-1):
                break
            else: return False
    print n
    msrTimer2 = timeit.default_timer()
    print "pembangkitan prima =",msrTimer2-msrTimer1,"s"
    return True

if __name__ == '__main__':
    print pengujianMSR(14087)