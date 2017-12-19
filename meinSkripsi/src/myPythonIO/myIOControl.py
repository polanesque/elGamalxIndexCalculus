'''
Created on Jan 11, 2017

@author: win3a1
'''
from java.io import FileReader, BufferedReader
#from java import FileReader, BufferedReader
from javax.swing import JFileChooser
from math import floor
#from IndexCalculus.step1 import 
#from myGUI.hackerFormWindow import gB, gP
import timeit
from __builtin__ import str

def myTimer():
    start = timeit.timeit()
    print "hello"
    end = timeit.timeit()
    return end - start

def expTester(a, b, p):
    return pow(a, b)%p

def fileBrowser():
    myFileChooser = JFileChooser()
    rVal = int(myFileChooser.showOpenDialog(None))
    print rVal
    if(rVal == JFileChooser.APPROVE_OPTION):
        theName = myFileChooser.getSelectedFile().getName()
        thePath = myFileChooser.getCurrentDirectory().toString()
        try:
            myPath =  theName + "/" + thePath
            
            fileReader = FileReader(myPath)
            bufferedReader = BufferedReader(fileReader)
            inputFile=""
            textFieldReadable = bufferedReader.readLine()
            while(textFieldReadable!=None):
                inputFile+=textFieldReadable
                inputFile+="\n"
            #    textFieldReadable = bufferedReader.readLine()
            #pesanAsli.text = inputFile
            return inputFile
            
        except(RuntimeError, TypeError, NameError):
                print "eror gan"


def parseTxtToWords(path):
    f = open(path, 'r')
    for line_no, line in enumerate(f):
        # Remember not to count the newline character
        if len(line.strip()) != 32:
            print line_no, line
    
    
    for line in f:
        for i in range(0, 3) and (line[i]!="    "):
            print line[i]
    return line
    f.close()

def arraySplitter(M):
    M2D = [[0 for j in range(2)] for i in range(len(M)/2)] #  [[0 for j in range(2)] for i in range((len(M))/2)]#[[0] * (len(M)/2)] * 2
    #print M2D
    i=0
    print len(M)
    j=0
    while i<len(M):
        ind = floor((i+1)/2)
        ind = int(ind)
        if(i % 2 == 0):
            M2D[j][0] = M[i]
        elif(i % 2 == 1):
            M2D[j][1] = M[i]
            j+=1
        i+=1
    return M2D

def returnItToString(M):
    i=0
    myString = ""
    for i in range(0,len(M)):
        myString = myString + str(unichr(M[i]))
    return myString
    
def cypherTxtToList(path):
    f = open(path)
    x = []
    for word in f.read().split():
        print(word)
        x.append(int(word))
    print x
    return x

def txtToWordsList(path):
    f = open(path)
    x = []
    for word in f.read().split():
        #print(word)
        x.append(word)
    print x
    
def saveDecryptedText(theString, myFile, myType):
    fileName = "D:\target/"+myFile+myType
    my_file = open(fileName,'w')
    my_file.write(theString)
    my_file.close()
    #
    f = open("test.txt","a") #opens file with name of "test.txt"
    f.write("and can I get some pickles on that")
    f.close()
    #

def kampfG(A, B, coef):
    x = ""
    x+=A
    x+=B
    x+=coef
    return x
def derDrucker(A, B, coef, ohm, randG, expo, Ax, gP, aP, Beta):
    dieString=""
    #temp=0
    """
    for i in range(0,len(B)):
        dieString+=str(coef[i])
        dieString+=" * log"
        dieString+=str(B[i])
        dieString+=" = "
        dieString+=str(coef[i])
        dieString+=" * "
        dieString+=str(A[i])
        dieString+=" = "
        dieString+=str(coef[i]*A[i])
        temp+=coef[i]*A[i]
        i+=1
    """
    
    dieString+="s = "
    dieString+=str(expo)
    dieString+="\n"
    
    
    dieString+=str(aP)#"alpha^"
    dieString+="^"
    dieString+=str(expo)
    dieString+=" = "
    dieString+=str(randG)
    dieString+=" mod "
    dieString+=str(gP)
    dieString+="\n"
    
    dieString+="Gamma = (Beta * alpha^s) mod p"
    dieString+="\n"
    
    dieString+="Gamma = "
    dieString+=str(Beta)
    #dieString+=str(1231)
    dieString+=" * "
    #dieString+=str(133)
    dieString+=str(randG)
    dieString+=" mod "
    dieString+=str(gP)
    #dieString+=str(gP)
    dieString+="\n"
    
    dieString+="Gamma = "
    dieString+=str(ohm)
    dieString+="\n"
    
    dieString+="Gamma = (c1 log p1 + c2 log p2 + ... + cn log pn)     mod p-1"
    dieString+="\n"
    
    dieString+="log Beta = (c1 log p1 + c2 log p2 + ... + cn log pn) - s    mod p-1"
    dieString+="\n"
    dieString+="log Beta = "
    
    j=0
    
    while(j<len(coef)):
        if(coef[j]>0):
            flag = True
            if(j>0):
                dieString+=" + "
            dieString+=str(coef[j])
            dieString+="log"
            dieString+=str(B[j])
        j+=1
        
    dieString+=" - "
    dieString+=str(expo)
    dieString+=" mod "
    dieString+=str(gP-1)
    dieString+="\n"
    dieString+="log Beta = "
    #dieString+="= "
    j=0
    while(j<len(coef)):
        if(coef[j]>0):
            if(j>0):
                dieString+=" + "
            dieString+=str(coef[j])
            dieString+="*"
            dieString+=str(A[j])
        j+=1
    dieString+=" - "
    dieString+=str(expo)
    dieString+=" mod "
    dieString+=str(gP-1)
    dieString+="\n"
    if(Ax!=int(Ax)):
        Ax = round(Ax, 3)
    else:
        Ax = int(Ax)
    dieString+="log Beta = "
    dieString+=str(Ax)
    
    return dieString

def derGMDdrucker(fBase, genMat, genGam):
    toPrint = ""
    
    toPrint+="\n"
    toPrint+="factor base"
    
    for i in range(0, len(genMat)):
        toPrint+="\t"
        toPrint+=str(fBase[i])
        i+=1
        if(i==len(genMat)):
            toPrint+="\t"
            toPrint+="Gamma"
    i=0
    toPrint+="\n"
    for i in range(0, len(genGam)):
        toPrint+="\n"
        toPrint+="\t\t"
        for j in range(0, len(genMat)):
            toPrint+=str(genMat[i][j])
            toPrint+="\t"
            j+=1
            if(j==len(genMat)):
                toPrint+=str(genGam[i])
                i+=1
                
    return toPrint

def derReddrucker(fBase, gReductedIC):
    toPrint = ""
    for i in range(0, len(gReductedIC)):
        toPrint+="log "
        toPrint+=str(fBase[i])
        toPrint+=" = "
        toPrint+=str(gReductedIC[i])
        toPrint+="\n"
        i+=1
    return toPrint


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd', 'e']
    b = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    c = ['sum1', 'sum2', 'sum3', 'sum4', 'sum5']
    print derGMDdrucker(a, b, c)
    
    print derReddrucker(a, c)
    