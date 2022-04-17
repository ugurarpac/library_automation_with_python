import sqlite3
import os
import subprocess
import webbrowser

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from logandregpage import *
from AnaSayfa import *
from tkinter import messagebox
from pynput.keyboard import Key, Controller

import sys
import urllib
import sqlite3

global curs
global conn
conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()
sorguCreTblkitaplik = ("CREATE TABLE IF NOT EXISTS kitap(                         \
                     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                      \
                     Nu TEXT NOT NULL,                         \
                     Adi TEXT NOT NULL,                        \
                     YazarAdi TEXT NOT NULL,                             \
                     Yayinevi TEXT NOT NULL,                             \
                     Tarih TEXT NOT NULL,                            \
                     Tur TEXT NOT NULL,                         \
                     Raf TEXT NOT NULL,                              \
                     Ayrac TEXT NOT NULL,                             \
                     Dil TEXT NOT NULL,                            \
                     Icerik TEXT                                     )")

curs.execute(sorguCreTblkitaplik)
conn.commit()


class LoginApp(QtWidgets.QWidget, Ui_Form, Ui_AnaSayfa):
    def reg(self):
        f_name = self.lineEdit_4.text()
        l_name = self.lineEdit_5.text()
        username = self.lineEdit_3.text()
        password = self.lineEdit_6.text()
        conf_pass = self.lineEdit_7.text()

        conn = sqlite3.connect('login_db.db')
        conn.execute('''INSERT INTO uyeler(first_name,last_name,username,password) VALUES(?,?,?,?)''',
                     (f_name, l_name, username, password))

        if (conf_pass != password):
            print(messagebox.askretrycancel(title="ERROR",
                                            message="Passwords are not matched. Try again"))
        else:
            print(messagebox.showinfo("Registration Successful","You can log in by going to the login page with the < button above."))


        conn.commit()

    def add(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        conn = sqlite3.connect('login_db.db')
        oku = conn.execute("SELECT count(*) as 'giris' FROM uyeler "
                           "WHERE username='" + username + "' AND password='" + password + "'")
        for i in oku.fetchall():
            giris = i[0]
        if (giris == 1):
            print("Welcome")
            os.system(r"C:\Users\HP\Desktop\pythonProject\ugur_project\output\main_ana\main_ana.exe")
            exit()
        else:
            print(messagebox.showinfo("ERROR","Your username or password is incorrect. Please try again."))

        conn.commit()

    def changeForm(self):
        if self.pushButton_7.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.pushButton_7.setText("<")
        else:
            self.widget_2.show()
            self.widget_3.hide()
            self.pushButton_7.setText(">")

    def open(self):
        webbrowser.open('https://www.linkedin.com/in/u%C4%9Fur-arpaci-9b109a156/')

    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_6.clicked.connect(self.reg)
        self.pushButton_5.clicked.connect(self.open)


        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.widget_3.hide()
        self.pushButton_7.clicked.connect(self.changeForm)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    app2 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AnaSayfa()
    ui.setupUi(MainWindow)

    sys.exit(app.exec_())
