# ch 8.1.3 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox, QLabel) # QLabel 추가
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore #모듈추가

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.lbl1 = QLabel('v2.3.0', self) # 버전 정보 표시를 위한 lbl1 위젯 생성
        self.btn1=QPushButton('Calc',self) # 버튼 이름 변경
        self.btn2=QPushButton('Clear',self)
        
        self.le1=QLineEdit('0', self) # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) #라인 에디트1 문자열 배치 설정
        self.le1.setFocus(True) # 포커스 설정
        self.le1.selectAll() # 텍스트 전체 선택

        self.le2=QLineEdit('0', self) # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) #라인 에디트2 문자열 배치 설정

        self.cb = QComboBox(self) # self.cb.addItems(['+', '-', '*', '/', '^', '%'])
        self.cb.addItems(['+', '-', '*', '/']) # ^와 % 연산자 제거

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.lbl1) # 버전 정보 표시를 위한 lbl1 위젯 생성
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox_formular = QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular) # hbox_formular 배치
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
    

    def setDisplay(self, text): # 함수명 변경
        self.te1.appendPlainText(text)
        
    def clearMessage(self):
        self.te1.clear()

   