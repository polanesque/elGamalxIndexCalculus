'''
Created on Sep 24, 2016

@author: win3a1
'''
from math import ceil, floor
import timeit
'''
Created on Sep 23, 2016

@author: win3a1
'''

from java import awt
from java.awt import Color, Font, TextArea
from javax.swing import JFrame, JButton, JLabel, JPanel, JOptionPane
from javax.swing import JFileChooser
from java.io import FileReader, BufferedReader
from myPythonIO import myIOControl as IOController
from ElGamal import elGamal
from myGUI import saveToFile
import gc

gB = 0
gP = 0

from IndexCalculus.step1 import IndexCalculusFinale #IndexCalculus.step1 import IndexCalculusFinale as keyBraker

myKey = JLabel("-")

def decryptMessage(event):
    
    myPK = [int(alphaTextField.text), int(betaTextField.text), int(primaTextField.text)]
    A = int(myKey.text)
    try:
        myPath = ""
        myPath = alamatFile.text
        myPath = alamatFile.text + "\\" + namaFile.text
        myPath = myPath.replace("\\","/")
        print "current path = ",myPath
        C = IOController.cypherTxtToList(myPath)
        print "C =",C
        C = IOController.arraySplitter(C)
        print "C2D = ",C
        M = elGamal.Dekripsi(myPK, C, A)
        print "hasil dekripsi =", M
        M = IOController.returnItToString(M)
        print "berhasil mengembalikan pesan =",M
        plainText.text = M
        myLabel.text = "Isi pesan asli"
        saveToFile.saveDecryptedText(M, "pesan setelah didekripsi", ".txt")
        JOptionPane.showMessageDialog(mainForm, "Berhasil mengembalikan pesan", "Info", JOptionPane.INFORMATION_MESSAGE)
    except:
        JOptionPane.showMessageDialog(mainForm, "Gagal mengenkripsi pesan", "Gagal!", JOptionPane.ERROR_MESSAGE)


formHeaderFont = awt.Font("Arial", Font.BOLD, 34)
regFont = awt.Font("Arial", Font.PLAIN, 13)
buttonFont = awt.Font("Tahoma", Font.BOLD, 21)
specialFont = awt.Font("Arial", Font.ITALIC, 13)
subSpecialFont = awt.Font("Courier", Font.PLAIN, 13)
boldenFont = awt.Font("Arial", Font.BOLD, 13)

def pelapor(event):
    from newForm import myNewForm    
    from newForm import generatedMatrix
    from newForm import eliminatedMatrix
    from newForm import finaleReport
    try:
        from IndexCalculus.step1 import gIC, gReductedIC, gFB, gGamma,\
    gRICsum, ohm, randomB, randomPow, gloc as A, primus as prime, akP, be
        from myPythonIO.myIOControl import derGMDdrucker, derReddrucker, derDrucker
        no1 = derGMDdrucker(gFB, gIC, gGamma)
        no2 = derReddrucker(gFB, gReductedIC)
        no3 = derDrucker(gReductedIC, gFB, gRICsum, ohm, randomB, randomPow, A, prime, akP, be) #(gReductedIC, gFB, gRICsum )
        logBundle=""
        import time
        if(myNewForm.isVisible()==True):
            myNewForm.show()
            generatedMatrix.text = no1
            eliminatedMatrix.text= no2
            finaleReport.text = no3
            finaleReport.revalidate
            logBundle = str(time.strftime("%d/%m/%Y"))
            logBundle+=" "
            logBundle+=str(time.strftime("%I:%M:%S"))
            logBundle+="\n"
            logBundle+= no1
            logBundle+="\n"
            logBundle+=no2
            logBundle+="\n"
            logBundle+=no3
            logBundle+="\n"
            saveToFile.saveDecryptedText(logBundle, "log", ".txt")
            gc.collect()
            print "i have been repainted"
        else:
            logBundle = str(time.strftime("%d/%m/%Y"))
            logBundle+=" "
            logBundle+=str(time.strftime("%I:%M:%S"))
            logBundle+="\n"
            logBundle+= no1
            logBundle+="\n"
            logBundle+=no2
            logBundle+="\n"
            logBundle+=no3
            logBundle+="\n"
            saveToFile.saveDecryptedText(logBundle, "log", ".txt")
            myNewForm.setVisible(True)
            gc.collect()
            print "mynewForm.visibility=",myNewForm.isVisible()
    except:
        print "gagal melaporkan"
    
def fileBrowser(event):
    myFileChooserX = JFileChooser()
    rValX = int(myFileChooserX.showOpenDialog(None))
    print "rVal =", rValX
    if(rValX == JFileChooser.APPROVE_OPTION):
        namaFile.text = myFileChooserX.getSelectedFile().getName()  
        alamatFile.text = myFileChooserX.getCurrentDirectory().toString()
        try:
            myPath =  alamatFile.text + "/" + namaFile.text
            fileReader = FileReader(myPath)
            print "mypath =", myPath
            bufferedReader = BufferedReader(fileReader)
            inputFile=""
            textFieldReadable = bufferedReader.readLine()
            while(textFieldReadable!=None):
                inputFile+=textFieldReadable
                inputFile+="\n"
                textFieldReadable = bufferedReader.readLine()
            print textFieldReadable
            #    textFieldReadable = bufferedReader.readLine()
            plainText.text = inputFile
            return inputFile
        except():#RuntimeError, TypeError, NameError):
                print "gagal mengembalikan pesan"




def react(event):
    myAlpha = int(alphaTextField.text)
    myBeta = int(betaTextField.text)
    myPrima = int(primaTextField.text)
    myS = int(FBSize.text)
    global gP
    gP = myPrima
    global gB
    gB = myBeta
    
    
    try:
        hackTimer0 = timeit.default_timer()
        hckd = 0
        hckd = IndexCalculusFinale(myBeta, myPrima, myAlpha, myS)
        
        hackTimer1 = timeit.default_timer()
        timeReporter="berhasil memecahkan kunci"
        timeReporter+="\n"
        timeReporter+="runtime ="
        timeReporter+=str(hackTimer1-hackTimer0)
        timeReporter+=" s"
        print "ez = ", hckd
        jack = ceil(hckd)
        print "jack =",jack
        jack = int(jack)
        print "jack2 =",jack
        
        witness = IOController.expTester(myAlpha, jack, myPrima)
        print  "witness = ",witness
        from IndexCalculus.step1 import gFB
        print "len =",len(gFB)
        #leng = len(gFB)
        #FBSize.text = str(leng) 
        hckd = round(hckd, 3)
        
        print "hckd =", str(hckd)
        if(witness==myBeta):
            JOptionPane.showMessageDialog(mainForm, timeReporter, "info", JOptionPane.INFORMATION_MESSAGE)
            hckd = floor(hckd)
            hckd = int(hckd)
            myKey.text = str(hckd)
        else:
            myKey.text = str(hckd)
            timeReporter="Kunci yang ditemukan tidak sesuai"
            timeReporter+="\n"
            timeReporter+="Runtime = "
            timeReporter+=str(hackTimer1-hackTimer0)
            timeReporter+=" s"
            JOptionPane.showMessageDialog(mainForm, timeReporter, "Pemberitahuan", JOptionPane.ERROR_MESSAGE)
    except:
        JOptionPane.showMessageDialog(mainForm, "Gagal memecahkan kunci", "Pemberitahuan", JOptionPane.ERROR_MESSAGE)
    
    
mainForm = JFrame("Hacker Form", size=(987, 610))

myPanel = JPanel()
myPanel.setOpaque(True)
myPanel.setBackground(Color.WHITE)
myPanel.setLayout(None)


# All Events Belong Here


# All Buttons Belong Here
hackButton = JButton("Pecahkan Kunci", actionPerformed=react)
hackButton.setSize(243,55)
hackButton.setLocation(62, 307)
hackButton.setFont(regFont)

laporan = JLabel("Laporan Pemecahan Kunci")
laporan.setSize(200, 21)
laporan.setLocation(26, 376)
laporan.setFont(boldenFont)

showReportButton = JButton("Tampilkan Matriks", actionPerformed=pelapor)
showReportButton.setSize(140, 21)
showReportButton.setLocation(157, 401)
showReportButton.setFont(regFont)

# All Text Fields Belong Here
pemecahanKunci = JLabel("Pemecahan kunci")
pemecahanKunci.setLocation(26, 91)
pemecahanKunci.setSize(130, 21)
pemecahanKunci.setFont(boldenFont)

alphaLabel = JLabel("Kunci publik alpha")
alphaLabel.setLocation(26, 122)#(26, 91)
alphaLabel.setSize(130, 21)
alphaLabel.setFont(regFont)

alphaTextField = awt.TextField("Alpha",10)
alphaTextField.setLocation(157, 122)#(157, 91)
alphaTextField.setSize(140, 21)
alphaTextField.setFont(regFont)

betaLabel = JLabel("Kunci publik beta")
betaLabel.setLocation(26, 159)
betaLabel.setSize(130, 21)
betaLabel.setFont(regFont)

betaTextField = awt.TextField("Beta",10)
betaTextField.setLocation(157, 159)
betaTextField.setSize(140, 21)
betaTextField.setFont(regFont)

primaLabel = JLabel("Prima")
primaLabel.setLocation(26, 193)
primaLabel.setSize(130, 21)
primaLabel.setFont(regFont)

primaTextField = awt.TextField("Prima",20)
primaTextField.setLocation(157, 193)
primaTextField.setSize(140, 21)
primaTextField.setFont(regFont)

"""
dekomposisiLabel = JLabel("Dekomposisi")
dekomposisiLabel.setLocation(26, 180)
dekomposisiLabel.setSize(130, 21)
dekomposisiLabel.setFont(regFont)

dekomposisiList = awt.List(5, False)
dekomposisiList.add("Cholesky")
dekomposisiList.add("LU Decomposition")
dekomposisiList.add("QR Decomposition")
dekomposisiList.setSize(140, 21)
dekomposisiList.setLocation(157, 180)
dekomposisiList.setFont(regFont)
"""
FBSizeLabel = JLabel("Batas Factor Base")
FBSizeLabel.setLocation(26, 227)
FBSizeLabel.setSize(130,21)
FBSizeLabel.setFont(regFont)

#FBSize = JLabel("n/a")
FBSize = awt.TextField("", 20)#JLabel("n/a")
FBSize.setLocation(157, 227)
FBSize.setSize(140, 21)
FBSize.setFont(regFont)

myKeyLabel = JLabel("Kunci privat")
myKeyLabel.setSize(130, 21)
myKeyLabel.setFont(regFont)
myKeyLabel.setLocation(26, 267)

#myKey = JLabel("-")
myKey.setSize(130, 30)
myKey.setFont(buttonFont)
myKey.setLocation(151, 267)

dekripsiLabel = JLabel("Dekripsi Pesan")
dekripsiLabel.setSize(140,21)
dekripsiLabel.setFont(boldenFont)
dekripsiLabel.setLocation(328, 91)#(26, 370)

pesanTerkunci = JLabel("Pesan terenkripsi")
pesanTerkunci.setSize(140,21)
pesanTerkunci.setFont(regFont)
pesanTerkunci.setLocation(328, 125)#(26, 399)

searchButton = JButton("Cari pesan", actionPerformed = fileBrowser)
searchButton.setFont(regFont)
searchButton.setSize(100, 21)
searchButton.setLocation(483, 125)


#(328, 91)

namaFile = JLabel("n/a")
namaFile.setFont(regFont)
namaFile.setSize(140,21)
namaFile.setLocation(483, 154)

alamatFile = JLabel("n/a")
alamatFile.setFont(regFont)
alamatFile.setSize(140,21)
alamatFile.setLocation(483, 183)

hDekripsiButton = JButton("Dekripsi Pesan", actionPerformed=decryptMessage)
hDekripsiButton.setFont(buttonFont)
hDekripsiButton.setSize(243, 55)
hDekripsiButton.setLocation(346, 225)#307)

#myTable.setSize(300, 400)
#myTable.setAutoResizeMode(JTable.AUTO_RESIZE_OFF)

myLabel = JLabel("Isi pesan terenkripsi")
myLabel.setFont(specialFont)
myLabel.setLocation(642, 91)
myLabel.setSize(200, 20)


plainText = TextArea("n/a")
plainText.setSize(300, 400)
plainText.setLocation(642, 114)
plainText.setFont(subSpecialFont)

# All Labels Belongs Here

hackingHeader = JLabel("<html><center>Hacker Form<html>", JLabel.CENTER)
hackingHeader.setSize(924, 55)
hackingHeader.setFont(formHeaderFont)
hackingHeader.setAlignmentY(34)
hackingHeader.setLocation(21, 21)


# All Form Belong Here
mainForm.setContentPane(myPanel)
mainForm.locationByPlatform = True


# Put Objects Altogether on Panel
myPanel.add(alphaTextField)
myPanel.add(hackButton)
myPanel.add(alphaLabel)
myPanel.add(betaLabel)
myPanel.add(primaLabel)
myPanel.add(betaTextField)
myPanel.add(primaTextField)
myPanel.add(hackingHeader)
#myPanel.add(dekomposisiLabel)
#myPanel.add(dekomposisiList)
myPanel.add(FBSizeLabel)
myPanel.add(FBSize)
myPanel.add(myKey)
myPanel.add(myKeyLabel)
#myPanel.add(encryptedText)
myPanel.add(plainText)
myPanel.add(dekripsiLabel)
myPanel.add(pesanTerkunci)
myPanel.add(searchButton)
myPanel.add(namaFile)
myPanel.add(alamatFile)
myPanel.add(hDekripsiButton)
#myPanel.add(myScrollPane)
myPanel.add(myLabel)
myPanel.add(laporan)
myPanel.add(showReportButton)
myPanel.add(pemecahanKunci)
#here

if(betaTextField.getText()== "" or alphaTextField.getText()== "" or primaTextField.getText()== ""):
    hackButton.setEnabled(False)
mainForm.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE)    
mainForm.visible = True    
myPanel.visible = True