'''
Created on Sep 24, 2016

@author: win3a1
'''
import timeit
from javax.swing import JFrame, JButton, JLabel, JPanel, JFileChooser, JScrollPane, JOptionPane,\
    JTabbedPane
from java.awt import Color, Font, BorderLayout
from java import awt
from java.io import FileReader, BufferedReader
from ElGamal import elGamal
from myPythonIO import myIOControl as IOController, myIOControl
from myGUI import saveToFile
subSpecialFont = awt.Font("Courier", Font.PLAIN, 13)
global myPath

def writeToTxt(theString, myFile, myType):
    try:
        namae = 'D:/target/'
        namae = namae + myFile
        namae = namae + myType
        my_file = open(namae,'w')
        my_file.write(theString)
        my_file.close()
    except:
        JOptionPane.showMessageDialog(naiveForm, "gagal menyimpan pesan ke txt", "info", JOptionPane.INFORMATION_MESSAGE)
    
def writeTxt(yourPath, yourString):
    try:
        print yourPath
        with open(yourPath, "a") as f:
            f.write(yourString)
    except:
        print "Gagal menulis pesan terenkripsi"
        
formHeaderFont = awt.Font("Arial", Font.BOLD, 34)
global regFont
regFont = awt.Font("Arial", Font.PLAIN, 13)
buttonFont = awt.Font("Arial", Font.BOLD, 21)
specialFont = awt.Font("Arial", Font.ITALIC, 13)

"""
def myDocReader(getpath):
    file = File(Null)
    extractor = WordExtractor(None)
    try:
        #file = File(path)
        fis = FileInputStream(getpath)
        document = HWPFDocument(fis)
        extractor = WordExtractor(document)
        fileData = extractor.getParagraphText()
        for i in range(0, fileata.length):
            if(fileData[i]!=0):
                #add to myString
    except:
        None
"""

def searchFile(event):
    myFileChooser = JFileChooser()
    rVal = int(myFileChooser.showOpenDialog(None))
    print rVal
    if(rVal == JFileChooser.APPROVE_OPTION):
        plainTextFile.text = myFileChooser.getSelectedFile().getName()
        plainTextPath.text = myFileChooser.getCurrentDirectory().toString()
        try:
            
            myPath =  plainTextPath.text + "/" + plainTextFile.text
            fileReader = FileReader(myPath)
            bufferedReader = BufferedReader(fileReader)
            inputFile=""
            textFieldReadable = bufferedReader.readLine()
            while(textFieldReadable!=None):
                inputFile+=textFieldReadable
                inputFile+="\n"
                textFieldReadable = bufferedReader.readLine()
            pesanAsli.text = inputFile
            
        except(RuntimeError, TypeError, NameError):
                print "eror gan"
            
def searchFile2(event):
    label3.text = "Isi pesan terenkripsi"
    label4.text = "Isi pesan asli"
    myFileChooser = JFileChooser()
    rVal = int(myFileChooser.showOpenDialog(None))
    print rVal
    if(rVal == JFileChooser.APPROVE_OPTION):
        encryptedTextFile.text = myFileChooser.getSelectedFile().getName()
        encryptedTextPath.text = myFileChooser.getCurrentDirectory().toString()
        try:
            myPath =  encryptedTextPath.text + "/" + encryptedTextFile.text
            fileReaderX = FileReader(myPath)
            bufferedReaderX = BufferedReader(fileReaderX)
            inputFile=""
            textFieldReadable = bufferedReaderX.readLine()
            while(textFieldReadable!=None):
                inputFile+=textFieldReadable
                inputFile+="\n"
                textFieldReadable = bufferedReaderX.readLine()
            pesanAsli.text = inputFile
            
            import myGUI.saveToFile as convertThis
            
            return convertThis.convertBackToInt(inputFile)
            
        except(RuntimeError, TypeError, NameError):
                print "eror gan"

            

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

def parseMyStringToInt(message):
    MyExString = list(message)
    i=0
    """while(i<len(MyExString) and ord(MyExString[i])!=10 and ord(MyExString[i])!=32):
        theLen=i
    """
    results = len(MyExString)*[None]
    while(i<len(MyExString)):
        results[i] = ord(MyExString[i])
        i+=1
    return results

def keyGeneration(event):
    try:
        kGenStart = timeit.default_timer()
        bP = int(bitPrima.text)
        A = int(kunciPrivatTextBox.text)
        KPEG = elGamal.keyGenerating(bP, A)
        print KPEG
        alpha.text = str(KPEG[0])
        beta.text = str(KPEG[1])
        genPrima.text = str(KPEG[2])
        print "t1"
        kGenStop  = timeit.default_timer()
        myMessage = "pembangkitan kunci "
        myMessage += str(bP)
        myMessage+=" bit berhasil"
        myMessage+="\nrunning time = "
        myMessage+=str(kGenStop - kGenStart)
        myMessage+=" detik"
        print "t2"
        JOptionPane.showMessageDialog(naiveForm, myMessage, "info", JOptionPane.INFORMATION_MESSAGE)
    except:
        JOptionPane.showMessageDialog(naiveForm, "gagal", "gagal membangkitkan kunci", JOptionPane.ERROR_MESSAGE)

def encryptMessage(event):
    try:
        eStart = timeit.default_timer()
        print "initiating"
        intToPrint=""
        publicKey = [int(alpha.text), int(beta.text), int(genPrima.text)]
        message = parseMyStringToInt(pesanAsli.text)
        encryptedMessage = elGamal.Enkripsi(publicKey, message)
        c=0
        myString = ''
        while(c<len(message)):
            myString+=str(encryptedMessage[c][0])
            myString+=str(encryptedMessage[c][1])
            if(c%5==0):
                    intToPrint+="\n"
            intToPrint+=str(encryptedMessage[c][0])
            intToPrint+=" "
            intToPrint+=str(encryptedMessage[c][1])
            intToPrint+=" "
            c+=1
        pesanTerenkripsi.setText("")
        pesanTerenkripsi.text = intToPrint
        writeToTxt(intToPrint, 'encryptedText', '.txt')
        eEnd = timeit.default_timer()
        tTp = "berhasil melakukan enkripsi pesan\n"
        tTp+="running time = "
        tTp+=str(eEnd - eStart)
        tTp+=" detik"
        JOptionPane.showMessageDialog(naiveForm, tTp, "info", JOptionPane.INFORMATION_MESSAGE)
    except:
        JOptionPane.showMessageDialog(naiveForm, "ada kesalahan", "info", JOptionPane.ERROR_MESSAGE)
        
def decryptMessage(event):
    myPK = [int(alpha.text), int(beta.text), int(genPrima.text)]
    A = int(privateKeyTextBox.text)
    
    
    try:
        myPath = ""
        myPath = encryptedTextPath.text
        myPath = encryptedTextPath.text + "\\" + encryptedTextFile.text
        myPath = myPath.replace("\\","/")
        #print "current path = ",myPath
        C = IOController.cypherTxtToList(myPath)
        #print "C =",C
        C = IOController.arraySplitter(C)
        #print "C2D = ",C
        dStart = timeit.default_timer()
        M = elGamal.Dekripsi(myPK, C, A)
        dEnd = timeit.default_timer()
        #print "hasil dekripsi =", M
        M = myIOControl.returnItToString(M)
        print "berhasil mengembalikan pesan M = \n",M
        pesanTerenkripsi.text = M
        saveToFile.saveDecryptedText(M, "pesan asli", ".txt")
        tTpD = "berhasil mengembalikan pesan"
        tTpD+="\nrunning time = "
        tTpD+=str(dEnd - dStart)
        tTpD+=" detik"
        print tTpD
        JOptionPane.showMessageDialog(naiveForm, tTpD, "info", JOptionPane.INFORMATION_MESSAGE)
        #JOptionPane.showMessageDialog(naiveForm, "Gagal mengenkripsi pesan", "Gagal!", JOptionPane.ERROR_MESSAGE)
    except:
        JOptionPane.showMessageDialog(naiveForm, "Gagal mengenkripsi pesan", "Gagal!", JOptionPane.ERROR_MESSAGE)
        
def printToTextArea(event):
    try:
        myPath =  plainTextPath.text + "/" + plainTextFile.text
        fileReader = FileReader(myPath)
        bufferedReader = BufferedReader(fileReader)
        inputFile=""
        intToPrint=""
        myString=""
        textFieldReadable = bufferedReader.readLine()
        while(textFieldReadable!=None):
            inputFile+=textFieldReadable
            inputFile+="\n"
            textFieldReadable = bufferedReader.readLine()
        pesanAsli.text = inputFile
        thisInt = parseMyStringToInt(inputFile)
        elGamalPK = [int(alpha.text), int(beta.text), int(genPrima.text)]
        encryptedMessage = elGamal.Enkripsi(elGamalPK, thisInt)
        #thisInt = thisFoo(inputFile)
        for i in range (0, (len(thisInt)-1)):
                intToPrint+=encryptedMessage[i][0],
                myString+=encryptedMessage[i][0] 
                
                intToPrint+=encryptedMessage[i][1]
                myString+=encryptedMessage[i][1]
                if(i%5==0):
                    intToPrint+="\n"
           
        print "ini pesan:",intToPrint
        pesanTerenkripsi.setText("")
        pesanTerenkripsi.text = intToPrint
    except(RuntimeError, TypeError, NameError):
        print "eror gan"

naiveForm = JFrame("Naive Form", size=(987, 610))
naiveFormPanel = JPanel()
naiveFormPanel.setLocation(0, 0)
naiveFormPanel.setOpaque(True)
naiveFormPanel.setBackground(Color.WHITE)
naiveFormPanel.setLayout(None)

# All Text Fields Belong Here
betaTextField = awt.TextField(20)
betaTextField.setLocation(454, 278)
betaTextField.setSize(233, 13)
betaTextField.setFont(regFont)

primaTextField = awt.TextField(20)
primaTextField.setLocation(454, 325)
primaTextField.setSize(233, 34)
primaTextField.setFont(regFont)


# All Labels Belongs Here
naiveHeader = JLabel("<html><center>Naive Form<html>",  JLabel.CENTER)
naiveHeader.setSize(924, 55)
naiveHeader.setFont(formHeaderFont)
naiveHeader.setLocation(21, 21)
#naiveHeader.setBorder(BorderFactory.createLineBorder(Color.BLACK))

label1 = JLabel("Pembangkitan Kunci")
label1.setFont(specialFont)
label1.setSize(140, 15)
label1.setLocation(21, 91)

#bit Prima
bitPrimaLabel = JLabel("bit Prima")
bitPrimaLabel.setLocation(26, 114)
bitPrimaLabel.setSize(100, 13)
bitPrimaLabel.setFont(regFont)

bitPrima = awt.TextField(10)
bitPrima.setLocation(157, 114)
bitPrima.setSize(100, 21)
bitPrima.setFont(regFont)

#kunci Privat
kunciPrivatLabel = JLabel("A")
kunciPrivatLabel.setLocation(26, 138)
kunciPrivatLabel.setSize(100, 13)
kunciPrivatLabel.setFont(regFont)

kunciPrivatTextBox = awt.TextField(10)
kunciPrivatTextBox.setLocation(157, 136)
kunciPrivatTextBox.setSize(100, 21)
kunciPrivatTextBox.setFont(regFont)


#prima
primaLabel = JLabel("Prima")
primaLabel.setLocation(26, 158)
primaLabel.setSize(100, 13)
primaLabel.setFont(regFont)

genPrima = JLabel("n/a")
genPrima.setLocation(157, 158)
genPrima.setSize(180, 13)
genPrima.setFont(regFont)

#alpha
aphaLabel = JLabel("Alpha")
aphaLabel.setLocation(26, 180)
aphaLabel.setSize(100, 13)
aphaLabel.setFont(regFont)

alpha = JLabel("n/a")
alpha.setSize(180,13)
alpha.setLocation(157, 180)
alpha.setFont(regFont)

#alpha^A
betaLabel = JLabel("Alpha^A")
betaLabel.setSize(180, 13)
betaLabel.setLocation(26, 202)
betaLabel.setFont(regFont)

beta = JLabel("n/a")
beta.setSize(180,13)
beta.setLocation(157, 202)
beta.setFont(regFont)

#tombol copy to clipboard
genKeyButton = JButton("Bangkitkan kunci", actionPerformed=keyGeneration)
genKeyButton.setSize(243,55)
genKeyButton.setLocation(62, 223)
genKeyButton.setFont(buttonFont)


#tabbed pane enkripsi dan dekripsi
myTabbedPane = JTabbedPane()
myTabbedPane.setSize(310, 214)
myTabbedPane.setLocation(21, 299)

#global regFont
#regFont = awt.Font("Arial", Font.PLAIN, 13)

#panel1
panel1 = JPanel()
panel1.setOpaque(True)
panel1.setBackground(Color.WHITE)
panel1.setLayout(None)
myTabbedPane.addTab("Enkripsi", panel1)
panel1.setSize(393, 214)
panel1.setLocation(0, 0)

plainTextLabel = JLabel("Pesan asli")
plainTextLabel.setSize(140,15)
plainTextLabel.setLocation(13, 13)
plainTextLabel.setFont(regFont)

cariPesanButton = JButton("cari pesan", actionPerformed=searchFile)
cariPesanButton.setSize(100, 20)
cariPesanButton.setLocation(166, 13) #y=308
cariPesanButton.setFont(regFont)

plainTextFile = JLabel("n/a")
plainTextFile.setSize(143,15)
plainTextFile.setLocation(166, 41)
#plainTextFile.setFont(regFont)

plainTextPath = JLabel("n/a")
plainTextPath.setSize(143, 15)
plainTextPath.setLocation(166, 61)
#plainTextPath.font(regFont)

enkripsiButton = JButton("Enkripsi pesan", actionPerformed=encryptMessage)
enkripsiButton.setSize(243,55)
enkripsiButton.setLocation(31, 89)
enkripsiButton.setFont(buttonFont)

panel1.add(plainTextLabel)
panel1.add(cariPesanButton)
panel1.add(plainTextFile)
panel1.add(plainTextPath)
panel1.add(enkripsiButton)


panel2 = JPanel()
myTabbedPane.addTab("Dekripsi", panel2)
panel2.setSize(393, 214)
panel2.setLocation(0, 0)
panel2.setOpaque(True)
panel2.setBackground(Color.WHITE)
panel2.setLayout(None)


encryptedTextLabel = JLabel("Pesan terenkripsi")
encryptedTextLabel.setSize(140,15)
encryptedTextLabel.setLocation(13, 13)
encryptedTextLabel.setFont(regFont)


cariPesanButton = JButton("cari pesan", actionPerformed=searchFile2)
cariPesanButton.setSize(100, 20)
cariPesanButton.setLocation(166, 13)
cariPesanButton.setFont(regFont)


encryptedTextFile = JLabel("n/a")
encryptedTextFile.setSize(140,15)
encryptedTextFile.setLocation(166, 41)
encryptedTextPath = JLabel("n/a")
encryptedTextPath.setSize(140, 15)
encryptedTextPath.setLocation(166, 61)


privateKeyLabel = JLabel("Kunci privat A")
privateKeyLabel.setSize(100, 15)
privateKeyLabel.setLocation(13, 85)
privateKeyLabel.setFont(regFont)

privateKeyTextBox = awt.TextField(10)
privateKeyTextBox.setSize(100, 20)
privateKeyTextBox.setLocation(166, 85)

dekripsiButton = JButton("Dekripsi pesan", actionPerformed=decryptMessage)
dekripsiButton.setSize(243,55)
dekripsiButton.setLocation(31, 118)
dekripsiButton.setFont(buttonFont)

panel2.add(encryptedTextLabel)
panel2.add(cariPesanButton)
panel2.add(encryptedTextFile)
panel2.add(encryptedTextPath)
panel2.add(dekripsiButton)
panel2.add(privateKeyLabel)
panel2.add(privateKeyTextBox)

#label3
label3 = JLabel("Isi pesan asli")
label3.setFont(specialFont)
label3.setSize(140, 15)
label3.setLocation(358, 91)

#label4
label4 = JLabel("Isi pesan terenkripsi")
label4.setFont(specialFont)
label4.setSize(140, 15)
label4.setLocation(642, 91)

#text area pesan asli
pesanAsli = awt.TextArea("n/a",5,30)
pesanAsli.setLocation(363, 114)
pesanAsli.setSize(258, 400)
pesanAsli.setBackground(Color.GRAY)
pesanAsli.setFont(subSpecialFont)

pesanAsli.setEditable(False)
scrollPanePTx = JScrollPane(pesanAsli)
pesanAsli.setColumns(100)
pesanAsli.setRows(200)


pesanTerenkripsi = awt.TextArea("n/a",5,30)
pesanTerenkripsi.setLocation(647, 114)
pesanTerenkripsi.setSize(258, 400)
pesanTerenkripsi.setBackground(Color.GRAY)
pesanTerenkripsi.setFont(subSpecialFont)
pesanTerenkripsi.setEditable(False)
scrollPaneCTx = JScrollPane(pesanTerenkripsi)
pesanTerenkripsi.setColumns(100)
pesanTerenkripsi.setRows(200)




# All Form Belong Here
naiveForm.setContentPane(naiveFormPanel)
naiveForm.locationByPlatform = True


# Put Objects Altogether on Panel
naiveFormPanel.add(naiveHeader, BorderLayout.CENTER)
naiveForm.add(myTabbedPane)
naiveFormPanel.add(primaLabel)
naiveFormPanel.add(aphaLabel)
naiveFormPanel.add(bitPrimaLabel)
naiveFormPanel.add(label1)
naiveFormPanel.add(betaLabel)
naiveFormPanel.add(bitPrima)
naiveFormPanel.add(genPrima)
naiveFormPanel.add(alpha)

alpha.text = "20135"
beta.text = "17096"
genPrima.text = "90059"


naiveFormPanel.add(beta)
naiveFormPanel.add(genKeyButton)
naiveFormPanel.add(kunciPrivatLabel)
naiveFormPanel.add(kunciPrivatTextBox)
naiveFormPanel.add(label3)
naiveFormPanel.add(label4)
naiveFormPanel.add(pesanAsli)
naiveFormPanel.add(scrollPanePTx)
naiveFormPanel.add(pesanTerenkripsi)
naiveFormPanel.add(scrollPaneCTx)

naiveForm.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE)
naiveForm.visible = True    
naiveFormPanel.visible = True