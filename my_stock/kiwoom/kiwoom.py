from PyQt5.QAxContainer import *


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        
        print('Kiwoom class 입니다.')
        
        self.get_ocx_instance()
        self.event_slots()
        
        self.signal_login_commConnect()
     
        
    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
      
        
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
       
        
    def login_slot(self, erroCode):
        print(erroCode)
        
        
    def signal_login_commConnect(self):
        self.dynamilcCall("CommConnect()")