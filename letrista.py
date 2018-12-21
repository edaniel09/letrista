import sys
import os
import random
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSlider
from PyQt5.uic import loadUi
from lib.trasformaciones import *
#import transformaciones as trans

class Letrista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('letrista.ui', self)
        self.setFixedSize(self.size())
        list1 = [
            self.tr('Seleccione una regla'),
            self.tr('Palindromo'),
            self.tr('Reverso'),
            self.tr('No vocales'),
            self.tr('No consonantes'),
            self.tr('Shuffle'),
            self.tr('Ordenar letras')
            #agregar mas reglas
        ]
        list2 = [
            self.tr('Español Lat.'), 
            self.tr('Español España'),
            self.tr('Inglés'),
            self.tr('Alemán'),
            self.tr('Catalán'),
            self.tr('Danés'),
            self.tr('Griego'),
            self.tr('Francés'),
            self.tr('Italiano'),
            self.tr('Portugués'),
            #self.tr('Ruso'),
            self.tr('Turco'),
            self.tr('Vietnamés'),
            #self.tr('Mandarín'),
            self.tr('Latín')
        ]
        list3 = [
            self.tr('Masculino 1'),
            self.tr('Masculino 2'),
            self.tr('Masculino 3'),
            self.tr('Masculino 4'),
            self.tr('Masculino 5'),
            self.tr('Femenino 1'),
            self.tr('Femenino 2'),
            self.tr('Femenino 3'),
            self.tr('Femenino 4'),
            self.tr('Femenino 5')
        ]
        self.setWindowTitle('Letrista')
        self.comboBox.clear()
        self.comboBox.addItems(list1)
        self.comboBox2.addItems(list1)
        self.comboBox3.addItems(list1)
        self.comboBox4.addItems(list1)

        self.comboBoxLang.addItems(list2)
        self.comboBoxVoice.addItems(list3)

        self.hzslidervs.setTickPosition(QSlider.TicksBelow)
        self.hzslidervt.setTickPosition(QSlider.TicksBelow)
        
        self.hzslidervs.setValue(50)
        self.hzslidervt.setValue(50)
        #self.hzslidervs.setTickPosition(50)
        self.actionCargar_Archivo.triggered.connect(self.cargartxtCall)
        self.actionGuardar_Audio_Generado.triggered.connect(self.ttsSave)
        self.actionAbrir_ventana.triggered.connect(self.cargarVentana)
        self.actionSalir.triggered.connect(self.salirCall)
        self.btnaplicar.clicked.connect(self.onbtnaplicar)
        self.btnplay1.clicked.connect(self.onbtnplay1clicked)
        self.btnplay2.clicked.connect(self.onbtnplay2clicked)
        self.btnreplace.clicked.connect(self.onbtnreplaceclicked)
    @pyqtSlot()
    def tts(self, text):
        #cambiar idiomas de espeak y rangos de voz aleatoriamente
        #-s es para velocidad: 80 es el minimo 500 es el practico maximo
        speed = (self.hzslidervs.value() + 40)*2
        tono = self.hzslidervt.value()
        acentocb = str(self.comboBoxLang.currentText())
        acento = self.loadAcento(acentocb)
        vozcb = str(self.comboBoxVoice.currentText())
        voz = self.loadVoice(vozcb)
        return os.system("espeak -v"+acento+"+"+voz+" -k 1 -s "+str(speed)+" -p "+str(tono)+" "+text+" ")

    def ttsSave(self):
        text = self.txtres.toPlainText()
        #verificar si el campo esta vacio
        return os.system("espeak -ves-la -k 1 "+'"'+text+'"'+" --stdout > myaudio")

    def loadAcento(self, txt):
        if(txt == 'Español Lat.'):
            return "es-la"
        elif(txt == 'Español España'):
            return "es"
        elif(txt == 'Inglés'):
            return "en"
        elif(txt == 'Alemán'):
            return "de"
        elif(txt == 'Catalán'):
            return "ca"
        elif(txt == 'Danés'):
            return "da"
        elif(txt == 'Griego'):
            return "el"
        elif(txt == 'Francés'):
            return "fr-fr"
        elif(txt == 'Italiano'):
            return "it"
        elif(txt == 'Portugués'):
            return "pt-pt"
        elif(txt == 'Ruso'):
            return "ru"
        elif(txt == 'Turco'):
            return "tr"
        elif(txt == 'Vietnamés'):
            return "vi"
        elif(txt == 'Mandarín'):
            return "zh"
        elif(txt == 'Latín'):
            return "la"

    def loadVoice(self, txt):
        if(txt == 'Masculino 1'):
            return "m1"
        elif(txt == 'Masculino 2'):
            return "m2"
        elif(txt == 'Masculino 3'):
            return "m3"
        elif(txt == 'Masculino 4'):
            return "m4"
        elif(txt == 'Masculino 5'):
            return "m5"
        elif(txt == 'Femenino 1'):
            return "f1"
        elif(txt == 'Femenino 2'):
            return "f2"
        elif(txt == 'Femenino 3'):
            return "f3"
        elif(txt == 'Femenino 4'):
            return "f4"
        elif(txt == 'Femenino 5'):
            return "f5"

    def onbtnaplicar(self):
        text = self.txtload.toPlainText()
        textmod = self.letristaRule(text.lower(), 1)
        textmod2 = self.letristaRule(textmod.lower(), 2)
        textmod3 = self.letristaRule(textmod2.lower(), 3)
        textmod4 = self.letristaRule(textmod3.lower(), 4)
        self.txtres.setText(textmod4)

    def onbtnplay1clicked(self):
        message = self.txtload.toPlainText()
        self.tts('"'+message+'"')


    def onbtnplay2clicked(self):
        message = self.txtres.toPlainText()
        self.tts('"'+message+'"')

    def onbtnreplaceclicked(self):
        message = self.txtres.toPlainText()
        palabra1 = self.lineEdit1.text()
        palabra2 = self.lineEdit2.text()
        message = message.replace(palabra1, palabra2)
        self.txtres.setText(message)

    def letristaRule(self, linea, box):
        if(box==1):
            rule = str(self.comboBox.currentText())
        elif(box==2):
            rule = str(self.comboBox2.currentText())
        elif(box==3):
            rule = str(self.comboBox3.currentText())
        elif(box==4):
            rule = str(self.comboBox4.currentText())
        #si es palindromo
        if(rule == 'Palindromo'):
            return aplicar_palindromo(linea)
        #si es reverso
        elif(rule == 'Reverso'):
            return aplicar_reverso(linea)
        #si es sin vocales
        elif(rule == 'No vocales'):
            return aplicar_no_vocales(linea)
        #si es sin consonantes
        elif(rule == 'No consonantes'):
            return aplicar_no_consonantes(linea)
        #si es shuffle
        elif(rule == 'Shuffle'):
            return aplicar_shuffle(linea)
        elif(rule=='Ordenar letras'):
            return aplicar_orden_letras(linea)
       
        return linea

    def cargartxtCall(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Seleccione un archivo de texto", "", "Text Files (*.txt)")
        if filename:
            filehandler = open(filename, 'r')
            lines = filehandler.readlines()
            if lines:
                self.txtload.setText('')
                self.txtres.setText('')
            for line in lines:
                self.txtload.insertPlainText(line)
               
    def salirCall(self):
        sys.exit(0)

    def cargarVentana(self):
        dialog = Letrista()
        dialog.show()

app = QApplication(sys.argv)
widget = Letrista()
widget.show()
sys.exit(app.exec_())