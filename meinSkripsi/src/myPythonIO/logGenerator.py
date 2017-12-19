'''
Created on 31 Mei 2017

@author: A C E R
'''
import time
def hackLog(theString):
    logName = str(time.strftime("%d/%m/%Y"))
    logName+=" "
    logName+=str(time.strftime("%I:%M:%S"))
    myType = ".txt"
    fileName = "D:\target\log/"+logName+myType
    my_file = open(fileName,'w')
    my_file.write(theString)
    my_file.close()