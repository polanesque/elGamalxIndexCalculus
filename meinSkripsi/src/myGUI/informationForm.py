'''
Created on 28 Feb 2017

@author: A C E R
'''
from javax.swing import JFrame, JPanel, JTabbedPane
from java.awt import BorderLayout


informasi = JFrame("Informasi", size=(610, 610)) 
informasi.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)



informasiPane = JPanel()

informasiTabbedPane = JTabbedPane()
informasiTabbedPane.setSize(610, 600)
informasiTabbedPane.setLocation(0, 0)

#global regFont
#regFont = awt.Font("Arial", Font.PLAIN, 13)

#panel1
mainFormHelper = JPanel()
mainFormHelper.setOpaque(True)
mainFormHelper.setLayout(None)
informasiTabbedPane.addTab("Halaman Utama", mainFormHelper)
mainFormHelper.setSize(610, 599)
mainFormHelper.setLocation(0, 0)

naiveFormHelper = JPanel()
naiveFormHelper.setOpaque(True)
naiveFormHelper.setLayout(None)
informasiTabbedPane.addTab("Naive Form", naiveFormHelper)
naiveFormHelper.setSize(610, 599)
naiveFormHelper.setSize(0,0)

hackerFormHelper = JPanel()
hackerFormHelper.setOpaque(True)
hackerFormHelper.setLayout(None)
informasiTabbedPane.addTab("Hacker Form", hackerFormHelper)
hackerFormHelper.setSize(610, 599)
hackerFormHelper.setSize(0,0)

informasiPane.setVisible(True)
informasi.add(informasiPane, BorderLayout.CENTER)
informasi.setVisible(True)