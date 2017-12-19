'''
Created on Sep 19, 2016

@author: win3a1
'''
from random import randint

import akarPrimitifGauss as primitiveRoot
from java.math import BigInteger as nonExshaustingPrimeGenerator
import pengujianMillerSelfridgeRabin as primality


def keyGenerating(primeBit, A):
    myPK = [0,0,0]
    batasBawah = pow(2, (primeBit-1))
    up = primeBit
    batasAtas = (pow(2, up))
    batasAtas = batasAtas-1
    prime = randint(batasBawah, batasAtas)
    prime = nonExshaustingPrimeGenerator.valueOf(prime)
    #prime = nonExshaustingPrimeGenerator.nextProbablePrime(prime)
    while(primality.pengujianMSR(prime)==False):
        prime = nonExshaustingPrimeGenerator.nextProbablePrime(prime) #randint(batasBawah, batasAtas)
    prime = int(prime)
    alpha = primitiveRoot.GaussForPrimitiveRoot(prime)
    alpha_a = pow(alpha, A)
    alpha_a = alpha_a%prime
    myPK[0] = alpha
    myPK[1] = alpha_a
    myPK[2] = prime
    return myPK

def Enkripsi(publicKey, M):
    print M
    #ncols = len(M)
    #nrows = 2
    C = [[0 for j in range(2)] for i in range(len(M))]
    a = publicKey[0]
    aA = publicKey[1]
    p = publicKey[2]

    for i in range(0, len(M)):
        k = randint(2,p-2)
        C[i][0] = (pow(a,k))%p
        C[i][1] = (((pow(aA,k))%p)*(M[i]))%p
    print "C = ",C
    return C

def Dekripsi(publicKey, C, A):
    p = int(publicKey[2])
    print p
    M =range(len(C))
    #A = BigInteger.valueOf(A)
    print "C.length =", len(C)
    for i in range(0, len(C)):
        exp = p-1-A
        mytemp = pow(C[i][0], exp) % p
        M[i] = (mytemp * C[i][1])%p
        
    return M

if __name__ == '__main__':
    print keyGenerating(14, 100)
    #C2D = [[747, 264], [1079, 1249], [827, 1371], [1061, 531], [426, 273], [1014, 523], [483, 1050]]
    #pK = [697, 378, 1399]
    #A = 331
    #print Dekripsi(pK, C2D, A)