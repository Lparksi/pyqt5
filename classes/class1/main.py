# classes/class1/main.py

#!/usr/bin/python3
#-*- coding: utf-8 -*-

#以上两行分别代表：使用Python3（Linux下），使用“utf-8”以避免乱码
import  sys
from PyQt5.QtWidgets import QApplication, QWidget
#引入PyQt5.QtWidgets模块

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。
    # Python可以在shell里运行，这个参数提供对脚本控制的功能。
    w = QWidget()
    #QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，
    # 构造器是没有父级的，没有父级的构造器被称为窗口（window）。
    w.resize(250,150)
    #resize()方法改变控件的大小，你应该传入两个参数，即宽与高，这里为宽250px，高150px
    w.move(300,300)
    #move()方法能够改变控件的位置，注意！屏幕坐标系的原点在左上角！
    # 这里将控件移动到(300,3000)位置
    w.setWindowTitle('HelloWord')
    #setWindowTitle()方法改变窗口的标题，我们称为标题栏，
    # 这里修改为“HelloWord”
    w.show()
    #将控件在内存中创建，并显示在桌面上（初始化）

    sys.exit(app.exec_())
    #保证主控件安全退出，请使用exex_,
    # 因为exec是Python保留字！