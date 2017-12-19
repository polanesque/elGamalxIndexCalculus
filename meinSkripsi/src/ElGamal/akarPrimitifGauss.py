'''
Created on Sep 19, 2016

@author: win3a1
'''
from math import ceil
from math import sqrt
from random import randint
import timeit


def GaussForPrimitiveRoot(p):
    gaussTimer1 = timeit.default_timer()
    #x = p/100
    m = randint(2,p)
    t=1
    diekonter=0
    while(True):
        #print "m=",m
        thisList =[0]
        diekonter+=1
        while((pow(m,t)%p)!=1):
            thisList.append(pow(m,t)%p)
            t+=1
        if(t==p-1):
            gaussTimer2 = timeit.default_timer()
            print "pembangkitan alpha =",gaussTimer2-gaussTimer1,"s"
            return m
            
        else:
            #print "bukan m-",diekonter
            b = randint(2,p-2)
            while(thisList.count(b)>0):
                b = randint(2,p-2)
            #print "b =",b
            u = OrderCounter(b, p)
            print "u =",u
            if(u==p-1):
                #print "tapi b",diekonter
                gaussTimer2 = timeit.default_timer()
                print "pembangkitan alpha =",gaussTimer2-gaussTimer1,"s"
                return b
            else:
                #print "bukan b",diekonter
                v = lcm(t, u)
                #print "v=",v
                a = brent(v)
                c = v/a
                if(v==p-1):
                    #print "tapi m1b1-",diekonter
                    ap = pow(m,(t/a))%p
                    ap = (ap*(pow(b,(u/c)[p])))%p
                    gaussTimer2 = timeit.default_timer()
                    print "pembangkitan alpha =",gaussTimer2-gaussTimer1,"s"
                    return ap
                else:
                    #print "bukan m1b1",diekonter
                    del thisList
                    #v = t
                    m = ((pow(m,(t/a))%p)*(pow(b,(u/c))%p))%p
                    print "m",diekonter," yang baru =",m
                    pass
                pass
            pass
        continue    
                
def OrderCounter(alpha, p):
    order=1
    while((pow(alpha,order))%p!=1):
        order+=1
    return order

def gcd(x,y):
    while y > 0:
        x, y = y, x % y
    return x
    
def lcm(x, y):
    return (x*y)/( gcd(x, y))

def brent(N):
        #if N%2==0:
        #        return 2
        y,c,m = randint(1, N-1), randint(1, N-1), randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g

def FaktorisasiFermat(N):
    global factor1
    global factor2
    s = ceil(sqrt(N))
    u = (s*2)+1
    v = 1
    r = (s*s)-N
    while(r!=0):
        if(r>0):
            while(r>0):
                r = r - v
                v = v + 2
            continue
        else:
            r = r + u
            u = u + 2
            continue
    factor1 = ((u + v) - 2)/2
    factor2 = (u - v)/2
    
if __name__ == '__main__':
    print brent(7917)
    print GaussForPrimitiveRoot(1013)