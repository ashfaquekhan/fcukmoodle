import mss
import numpy as np
import sys
from pynput import keyboard
from pynput.keyboard import Controller
import pyperclip as pc 
screencap = mss.mss()
def screenshotRegion(screenRegion):
    return np.asarray(screencap.grab(screenRegion))

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        self.setWindowTitle("POCKETAPE")  
        self.setGeometry(50, 50, 300, 90) 
        self.button = QPushButton("PASTE", self) 
        self.button.setGeometry(90, 23, 100, 40) 
        self.button.setCheckable(True) 
        self.button.clicked.connect(self.changeColor) 
        self.setStyleSheet("background-color : black") 
        self.button.setStyleSheet("background-color : white")

        self.update() 
        self.show() 

    def changeColor(self): 
        kibord = Controller()
        def on_release(key):
            if key == keyboard.Key.esc:
                return False
            if key == keyboard.Key.f9: 
                cptext = pc.paste()     
                kibord.type(cptext)

        if self.button.isChecked(): 
            self.button.setStyleSheet("background-color : lightgreen") 
        else: 
            self.button.setStyleSheet("background-color : white") 
  
def on_release(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.f9: 
        cptext = pc.paste()     
        kibord.type(cptext)


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
    App = QApplication(sys.argv) 
    window = Window() 
    sys.exit(App.exec()) 
