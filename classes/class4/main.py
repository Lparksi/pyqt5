#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication

class CenterExample(QWidget):
    def __init__(self):
        super(CenterExample, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()
        # 执行我们写的居中方法
        self.setWindowTitle("Center")
        self.show()
    def center(self):
        qr = self.frameGeometry()
        # 获取主窗口大小
        cp =  QDesktopWidget().availableGeometry().center()
        # 获取屏幕分辨率并得到中间的位置
        qr.moveCenter(cp)
        # 将窗口的中心点放到屏幕的中间位置，
        # 这个方法貌似没有文档，IDE有可能没有补全
        self.move(qr.topLeft())
        # 然后把窗口的坐上角的坐标设置为qr的矩形左上角的坐标，这样就把窗口居中了。
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = CenterExample()
    sys.exit(app.exec_())