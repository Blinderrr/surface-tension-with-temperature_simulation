# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,  QMessageBox
from PyQt5.QtGui import QMovie
import sys
import matplotlib.pyplot as plt
import numpy as np
class Ui_one(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(600, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setEnabled(True)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget_5)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setDigitCount(10)
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.label_7=QtWidgets.QLabel(self.widget_5)
        self.label_7.setStyleSheet("font: 15pt \"Agency FB\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.widget_9 = QtWidgets.QWidget(self.widget_6)
        self.widget_9.setGeometry(QtCore.QRect(20, 10, 81, 301))
        self.widget_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_9.setObjectName("widget_9")
        self.verticalSlider = QtWidgets.QSlider(self.widget_9)
        self.verticalSlider.setGeometry(QtCore.QRect(10, 10, 61, 251))
        self.verticalSlider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.545, y1:0, x2:0.546, y2:1, stop:0 rgba(254, 103, 103, 255), stop:1 rgba(97, 105, 255, 255));")
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(80)
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.verticalSlider.setObjectName("verticalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_9)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 270, 51, 23))
        self.lcdNumber.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setGeometry(QtCore.QRect(83, 280, 61, 21))
        self.label_3.setStyleSheet("font: 11pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.widget_7)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        pixmap = QPixmap("1234.png")
        self.label_2.setPixmap(pixmap)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "表面张力"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "表面张力系数为"))
        self.label_3.setText(_translate("MainWindow", "℃"))
        self.label_7.setText(_translate("MainWindow", "mN/m"))
        self.pushButton.setText(_translate("MainWindow", "开始计算"))
        self.pushButton_2.setText(_translate("MainWindow", "切换模式"))


class first(QMainWindow, Ui_one):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.verticalSlider.valueChanged.connect(self.update_lcdNumber)
        self.pushButton.clicked.connect(self.start_calculation)  # 连接按钮点击信号到计算函数
        self.pushButton_2.clicked.connect(self.to2)
    def update_lcdNumber(self):
        value = self.verticalSlider.value()
        self.lcdNumber.display(value)

    def start_calculation(self):
        self.movie = QMovie("1234.gif")  # 创建QMovie对象
        self.label_2.setMovie(self.movie)  # 设置label_2显示动画
        self.movie.frameChanged.connect(self.check_last_frame)
        self.movie.start()  # 点击开始计算按钮时播放动画
    def to2(self):
        self.cirr=second()
        self.hide()
        self.cirr.show()
    def check_last_frame(self, frame_number):
        if frame_number == self.movie.frameCount() - 1:
            self.movie.stop()
            self.reset_movie()  # 计算并显示表面张力系数
    def reset_movie(self):
        value = self.verticalSlider.value()
        T = value
        sigma = 75.69 - 0.1413 * T - 0.0002985 * T ** 2
        self.lcdNumber_2.display(round(sigma, 6))  # 计算并显示表面张力系数，保留四位小数
class Ui_two(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(600, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 11pt \"Agency FB\";")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_5.setStyleSheet("font: 11pt \"Agency FB\";")
        self.verticalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        plt.figure(figsize=(6, 6))
        T = np.linspace(0, 80, 1000)
        sigma = 75.69 - 0.1413 * T - 0.0002985 * T ** 2
        plt.plot(T, sigma)
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Surface Tension Coefficient (mN/m)')
        plt.savefig('surface_tension_plot.png')
        self.label_3.setScaledContents(True)
        # 读取保存的图片并显示在label_3上
        pixmap = QPixmap('surface_tension_plot.png')
        self.label_3.setPixmap(pixmap)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "表面张力"))
        self.label_3.setText(_translate("MainWindow", "结果显示区"))
        self.label.setText(_translate("MainWindow", "温度输入"))
        self.label_4.setText(_translate("MainWindow", "℃"))
        self.label_2.setText(_translate("MainWindow", "表面张力系数"))
        self.label_5.setText(_translate("MainWindow", "mN/m"))
        self.pushButton.setText(_translate("MainWindow", "开始计算"))
        self.pushButton_2.setText(_translate("MainWindow", "切换模式"))
class second(QMainWindow, Ui_two):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绘制初始表面张力系数变化图

        self.pushButton.clicked.connect(self.start_calculation)
        self.pushButton_2.clicked.connect(self.to1)
    def start_calculation(self):
        temperature_str = self.lineEdit.text()
        sigma_str = self.lineEdit_2.text()

        # 检查输入是否合法
        if (temperature_str and sigma_str) or (not temperature_str and not sigma_str):
            QMessageBox.warning(self, "输入错误", "请仅输入温度或表面张力系数其中一个！")
            return
        elif temperature_str:
            try:
                T = float(temperature_str)
                if not (0 <= T <= 80):
                    QMessageBox.warning(self, "输入错误", "温度输入范围应在 0 到 80 之间！")
                    return
            except ValueError:
                QMessageBox.warning(self, "输入错误", "温度输入应为数字！")
                return

            sigma = 75.69 - 0.1413 * T - 0.0002985 * T ** 2
            self.lineEdit_2.setText(f"{sigma:.6f}")
            plt.figure(figsize=(6, 6))
            # 重新绘制包含输入值的表面张力系数变化图并保存为图片
            T_plot = np.linspace(0, 80, 1000)
            sigma_plot = 75.69 - 0.1413 * T_plot - 0.0002985 * T_plot ** 2
            plt.plot(T_plot, sigma_plot)
            plt.scatter(T, sigma, color='red')
            plt.xlabel('Temperature (°C)')
            plt.ylabel('Surface Tension Coefficient (mN/m)')
            plt.title('Surface Tension Coefficient vs Temperature')
            plt.savefig('surface_tension_plot_updated.png')

            self.label_3.setScaledContents(True)
            pixmap_updated = QPixmap('surface_tension_plot_updated.png')
            self.label_3.setPixmap(pixmap_updated)
        elif sigma_str:
            try:
                sigma = float(sigma_str)
            except ValueError:
                QMessageBox.warning(self, "输入错误", "表面张力系数输入应为数字！")
                return

            # 通过公式近似求解对应的温度值T
            plt.figure(figsize=(6, 6))
            T = (75.69 - sigma) / 0.1413
            self.lineEdit.setText(f"{T:.6f}")
            # 重新绘制包含输入值的表面张力系数变化图并保存为图片
            T_plot = np.linspace(0, 80, 1000)
            sigma_plot = 75.69 - 0.1413 * T_plot - 0.0002985 * T_plot ** 2
            plt.plot(T_plot, sigma_plot)
            plt.scatter(T, sigma, color='red')
            plt.xlabel('Temperature (°C)')
            plt.ylabel('Surface Tension Coefficient (mN/m)')
            plt.title('Surface Tension Coefficient vs Temperature')
            plt.savefig('surface_tension_plot_updated123.png')

            # 读取更新后的图片并显示在label_3上
            self.label_3.setScaledContents(True)
            pixmap_updated123 = QPixmap('surface_tension_plot_updated123.png')
            self.label_3.setPixmap(pixmap_updated123)
    def to1(self):
        self.cirr=first()
        self.hide()
        self.cirr.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = first()
    main.setWindowTitle("表面张力")
    main.show()
    sys.exit(app.exec_())