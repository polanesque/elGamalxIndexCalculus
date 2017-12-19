'''
Created on Nov 29, 2016

@author: win3a1

'''


#from java.io import BufferedWriter
#import json
#import aboutForm

def saveThis(theString, myFile, myType):
    fileName = "D:\target/pesan asli/"+myFile+myType
    my_file = open(fileName,'w')
    my_file.write(theString)
    my_file.close()

def saveDecryptedText(theString, myFile, myType):
    fileName = 'D:/target/'+myFile+myType
    #fileName = fileName.replace("\\","/")
    decfile = open(fileName,"w")
    decfile.write(theString)
    decfile.close()

def convertBackToInt(theString):
    theList = theString.split()
    myList = len(theList)*[0]
    for i in range(0, len(theList)):
        myList[i] = int(theList[i])
        return myList
