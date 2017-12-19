'''
Created on Sep 24, 2016

@author: win3a1
'''
'''

Created on Sep 23, 2016

@author: win3a1

'''
from javax.swing import JFrame, JLabel, JPanel, ImageIcon
from java.awt import Color, Font

theFont = Font("Arial", Font.BOLD, 19)
elFont = Font("Arial", Font.BOLD, 23)

aboutForm = JFrame("About", size=(610, 610))
aboutPanel = JPanel()

aboutPanel.setOpaque(True)
aboutPanel.setBackground(Color.WHITE)
aboutPanel.setLayout(None)



judul1Label = JLabel("<html><center>TEKNIK PEMECAHAN KUNCI ALGORITMA ELGAMAL<br>DENGAN METODE INDEX CALCULUS</html>", JLabel.CENTER)
#judul1Label.setOpaque(True)
judul1Label.setFont(theFont)
judul1Label.setSize(610, 70)
judul1Label.setLocation(0, 10)

skripsiLabel = JLabel("SKRIPSI", JLabel.CENTER)
skripsiLabel.setFont(theFont)
skripsiLabel.setSize(610, 50)
#skripsiLabel.setOpaque(True)
skripsiLabel.setLocation(0, 80)

logo = JLabel("<html><center></html>",JLabel.CENTER)
logoFakultas = ImageIcon("D:\\logo.jpg")
logo.setIcon(logoFakultas)
logo.setSize(610, 200)
logo.setLocation(0, 145)
#logo.setOpaque(True)

namaLabel =JLabel("<html><center>ERWIN M H SINAGA<br>111401067</center></html>", JLabel.CENTER)
namaLabel.setFont(theFont)
namaLabel.setSize(610, 50)
namaLabel.setLocation(0, 360)
#namaLabel.setOpaque(True)

prodiLabel = JLabel("<html><center>PROGRAM STUDI S1 ILMU KOMPUTER<br> \
                    FAKULTAS ILMU KOMPUTER DAN TEKNOLOGI INFORMASI<br> \
                    UNIVERSITAS SUMATERA UTARA<br> \
                    MEDAN<br> \
                    2017</center></html>", JLabel.CENTER)
prodiLabel.setFont(theFont)
prodiLabel.setSize(610, 162)
prodiLabel.setLocation(0, 410)
#prodiLabel.setOpaque(True)

aboutForm.locationByPlatform = True
aboutPanel.add(judul1Label)
aboutPanel.add(skripsiLabel)
aboutPanel.add(logo)
aboutPanel.add(namaLabel)
aboutPanel.add(prodiLabel)
#aboutPanel.setOpaque(True)
aboutForm.setContentPane(aboutPanel)# add(aboutPanel)
aboutForm.visible = True