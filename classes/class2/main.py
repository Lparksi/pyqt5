#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

class My_tooltip(QWidget):
    def __init__(self):
        super(My_tooltip, self).__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        #设置字体为10px的SansSerif字体

        self.setToolTip('This is a <b>ToolTip</b>')
        #创建背景提示框，区别请见图片

        btn = QPushButton('Button',self)
        #创建一个按钮btn
        btn.setToolTip('This is a <b>ToolTip2</b>')
        #为‘btn’按钮添加提示框
        btn.resize(btn.sizeHint())
        #设置按钮大小，这里使用默认大小
        btn.move(50,50)
        #移动到坐标系(控件)的(50,50)位置

        self.setGeometry(300,300,300,200)
        #位置及大小设置
        self.setWindowTitle('ToolTips')
        #设置标题
        self.show()
        #初始化

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My_tooltip()
    sys.exit(app.exec_())