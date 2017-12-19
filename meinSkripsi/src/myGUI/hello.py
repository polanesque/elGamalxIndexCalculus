'''
Created on Sep 23, 2016

@author: win3a1
'''
from java import awt
from java.awt import Color, Font
from javax.swing import JFrame, JButton, JLabel, JPanel


#from java.awt.BorderLayout import NORTH
#from java.awt.BorderLayout import CENTER
#import myGUI
myFont = awt.Font("Golden Ratio Demo",Font.BOLD,34)


def hackerButton(event):
    #mainForm.visible = False
    from myGUI import hackerFormWindow
    mainForm.dispose()
    hackerFormWindow.mainForm.setVisible(True)

def naiveButton(event):
    from myGUI import naiveFormWindow
    mainForm.dispose()
    naiveFormWindow.naiveForm.setVisible(True)

def helpButton(event):
    from myGUI import informationForm
    mainForm.dispose()
    informationForm.informasiPane.setVisible(True)

def aboutButton(event):
    from myGUI import aboutForm
    mainForm.dispose()
    aboutForm.aboutForm.setVisible(True) 

#form and panel construction
mainForm = JFrame("Halaman Utama", size=(987,610), )
myPanel = JPanel()
myPanel.setOpaque(True)
myPanel.setBackground(Color.WHITE)
myPanel.setLayout(None)

message = JLabel("<html><center>Teknik Pemecahan Kunci Algoritma ElGamal <br>Dengan Metode Index Calculus<html>", JLabel.CENTER)
message.setSize(987, 144)

message.setFont(myFont)
#message.setAlignmentX(433)
message.setAlignmentY(34)
mainForm.setContentPane(myPanel)
#mainForm.setSize(310, 125)
mainForm.locationByPlatform=True
mainForm.visible=True



#buttons creation
button1 = JButton("Naive User", actionPerformed=naiveButton)
button1.setSize(233,145)
button1.setLocation(226, 233)
button1.setFont(myFont)

button2 = JButton("Hacker", actionPerformed=hackerButton)
button2.setSize(233,145)
button2.setLocation(527, 233)
button2.setFont(myFont)

button3 = JButton("Tentang", actionPerformed = aboutButton)
button3.setSize(144, 55)
button3.setLocation(744, 470)

button4 = JButton("Tentang", actionPerformed = aboutButton)
button4.setSize(144, 55)
button4.setLocation(809, 500)
myPanel.add(message)
myPanel.add(button1)
myPanel.add(button2)
myPanel.add(button3)
#myPanel.add(button4)

#mainForm.visible = True
myPanel.visible=True