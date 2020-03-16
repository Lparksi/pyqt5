#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication

class CloseExample(QWidget):
    def __init__(self):
        super(CloseExample, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        # 设置大小、位置
        self.setWindowTitle('Message Box')
        # 设置名称
        self.show()
        # 初始化
    def closeEvent(self, event):
        # 这个方法复写父类的方法'closeEvent'
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.Yes | QMessageBox.No)
        # 重要！提醒的内容，从左到右：self,标题,提示内容,两个提示按钮
        if reply == QMessageBox.Yes:
            # 如果用户选择Yes
            event.accept()
            # 执行操作
        else:
            # 如果用户选择No
            event.ignore()
            # 关闭提示窗口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CloseExample()
    sys.exit(app.exec_())