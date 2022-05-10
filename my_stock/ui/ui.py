from kiwoom.kiwoom import *

import sys
from PyQt5.QtWidgets import *

class Ui_class():
    def __init__(self):
        print('UI 클래스입니다.')
        
        
        self.app = QApplication(sys.argv)        
        
        
        
        Kiwoom()
        
        self.app.exec_() #종료 되지 않게 함
        

        
