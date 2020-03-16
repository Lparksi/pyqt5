#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication

class ExitExample(QWidget):
    def __init__(self):
        super(ExitExample, self).__init__()
        self.initUI()
        # 执行我们自己的方法initUI()
    def initUI(self):
        qbtn =  QPushButton('Quit',self)
        # 创建qbtn这个按钮，名字为“Quit”，无父组件
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 将'qbtn'按钮绑定到'quit'函数
        # 当'qbtn'按钮被点击时，执行'quit'函数
        qbtn.resize((qbtn.sizeHint()))
        # 默认大小
        qbtn.move(50,50)
        # 将按钮移动到窗口的(50,50)位置

        self.setGeometry(300,300,250,150)
        # 窗口的位置以及大小
        self.setWindowTitle('Quit')
        # 窗口的标题
        self.show()
        # 初始化

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExitExample()
    sys.exit(app.exec_())