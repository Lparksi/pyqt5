#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class My_Icon(QWidget):
    #创建我们自己的类My_Icon,继承自QWidget
    def __init__(self):
        super(My_Icon, self).__init__()
        self.initUI()
        #调用我们自己的方法initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        #setGeometry()接收四个参数，分别是坐标x，y与窗口长，宽
        #也就是说setGeometry()实现了resize()和move()的功能！
        #这里将窗口放置到（300，300），长为300，宽为200
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icon.jpg'))
        #创建一个QIcon对象,接收一个路径参数
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My_Icon()
    sys.exit(app.exec_())