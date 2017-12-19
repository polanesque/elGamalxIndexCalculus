'''
Created on 6 Mar 2017

@author: earnwings
'''
from javax.swing import JFrame, JPanel, JScrollPane, JTabbedPane
from java.awt import Color
from java.awt import Font

from IndexCalculus.step1 import myReporter, gIC, gReductedIC, gFB, gGamma,\
    gRICsum, ohm, randomB, randomPow, gloc as A, primus as prime, akP, be

from myPythonIO.myIOControl import derGMDdrucker, derReddrucker, derDrucker
from java import awt



string1 = derGMDdrucker(gFB, gIC, gGamma)
print string1
string2 = derReddrucker(gFB, gReductedIC)
print string2

string3 = derDrucker(gReductedIC, gFB, gRICsum, ohm, randomB, randomPow, A, prime, akP, be) #(gReductedIC, gFB, gRICsum )

meinFont = Font("Arial", Font.PLAIN, 32)

#white = Color.WHITE()
#meinFont.setColor(Color.WHITE)
#myICTable = JTable()



tabbedPane = JTabbedPane()
tabbedPane.setSize(377, 377)
tabbedPane.setLocation(15, 5)
tabbedPane.setVisible(True)



#panel1
p1 = JPanel()
p1.setOpaque(True)
p1.setBackground(Color.WHITE)
p1.setLayout(None)
p1.setSize(357, 337)
p1.setLocation(0, 0)
p1.setVisible(True)


generatedMatrix = awt.TextArea("-",7,7)
scrollPane1 = JScrollPane(generatedMatrix)
try:
    generatedMatrix.text = string1#myIOControl.derDrucker(gIC, gFB, gGamma)
except:
    print "Gagal melaporkan tahap 1"
generatedMatrix.setSize(393, 331)
generatedMatrix.setLocation(5, 5)
generatedMatrix.setBackground(Color.GRAY)


p1.add(generatedMatrix)
p1.add(scrollPane1)

tabbedPane.addTab("Index Calculus Matrix", p1)


eliminatedMatrix = awt.TextArea("-",7,7)
eliminatedMatrix.setSize(363, 341)
eliminatedMatrix.setLocation(5, 5)
eliminatedMatrix.setBackground(Color.GRAY)
p2 = JPanel()
p2.setSize(363, 341)
p2.setLocation(0, 0)
p2.setOpaque(True)
p2.setBackground(Color.WHITE)
p2.setLayout(None)
p2.setVisible(True)
p2.add(eliminatedMatrix)
tabbedPane.addTab("Eliminated Matrix", p2)
try:
    eliminatedMatrix.text = string2
except:
    print "Gagal melaporkan tahap 2"

p3 = JPanel()
p3.setOpaque(True)
p3.setBackground(Color.WHITE)
p3.setLayout(None)
p3.setSize(357, 337)
p3.setVisible(True)
finaleReport = awt.TextArea("-",7,7)

try:
    finaleReport.text = string3
except:
    print "Gagal melaporkan tahap 3"
finaleReport.setSize(363, 341)
finaleReport.setLocation(5, 5)
finaleReport.setBackground(Color.GRAY)

p3.add(finaleReport)
tabbedPane.addTab("Tahap ke-3", p3)

#panel3.setLocation(0, 0)

##

myNewPanel = JPanel()
myNewPanel.setLocation(0, 0)
myNewPanel.setOpaque(True)
myNewPanel.setBackground(Color.WHITE)
myNewPanel.setLayout(None)


myNewForm = JFrame("Laporan", size=(425, 425)) #(377, 377)
myNewForm.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)

myNewForm.locationByPlatform = True
#myNewForm.setVisible(True)
myNewForm.setContentPane(myNewPanel)
myNewForm.add(tabbedPane)
