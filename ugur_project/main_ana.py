import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfa import *
import sqlite3
import os

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_AnaSayfa()
ui.setupUi(MainWindow)

global curs
global conn
conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()
sorguCreTblkitaplik = ("CREATE TABLE IF NOT EXISTS kitap(\
                     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                     Nu TEXT NOT NULL,\
                     Adi TEXT NOT NULL,\
                     YazarAdi TEXT NOT NULL,\
                     Yayinevi TEXT NOT NULL,\
                     Tarih TEXT NOT NULL,\
                     Tur TEXT NOT NULL,\
                     Raf TEXT NOT NULL,\
                     Ayrac TEXT NOT NULL,\
                     Dil TEXT NOT NULL,\
                     Icerik TEXT)")

curs.execute(sorguCreTblkitaplik)
conn.commit()

def EKLE():
    _lneNu = ui.lneNu.text()
    _lneAdi = ui.lneAdi.text()
    _lneYazarAdi = ui.lneYazarAdi.text()
    _lneYayinevi = ui.lneYayinevi.text()
    _cmbTarih = ui.cmbTarih.currentText()
    _lneTur = ui.lneTur.text()
    _spnRaf = ui.spnRaf.value()
    _cmbAyrac = ui.cmbAyrac.currentText()
    _lneDil = ui.lneDil.text()
    _lneIcerik = ui.lneIcerik.toPlainText()

    curs.execute("INSERT INTO kitap \
                         (Nu,Adi,YazarAdi,Yayinevi,Tarih,Tur,Raf,Ayrac,Dil,Icerik) \
                          VALUES(?,?,?,?,?,?,?,?,?,?)", \
                 (_lneNu, _lneAdi, _lneYazarAdi, _lneYayinevi, _cmbTarih, _lneTur, _spnRaf, _cmbAyrac, _lneDil,
                  _lneIcerik,))

    conn.commit()
    LISTELE()


def LISTELE():
    ui.tblwBilgi.clear()
    ui.tblwBilgi.setHorizontalHeaderLabels(("No", 'Number', 'Book Name', 'Author', \
                                            'Publishing House', 'Release Date', 'Type', \
                                            'Shelf Number', 'Shelf Bracket', 'Language', 'Content'))

    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    curs.execute("SELECT * FROM kitap")

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwBilgi.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    ui.lneNu.clear()
    ui.lneAdi.clear()
    ui.lneYazarAdi.clear()
    ui.lneYayinevi.clear()
    ui.cmbTarih.setCurrentIndex(-1)
    ui.lneTur.clear()
    ui.spnRaf.setValue(55)
    ui.cmbAyrac.setCurrentIndex(-1)
    ui.lneDil.clear()
    ui.lneIcerik.clear()

    curs.execute("SELECT COUNT(*) FROM kitap")
    kayitSayisi = curs.fetchone()
    ui.lblKayitSayisi.setText(str(kayitSayisi[0]))


LISTELE()


def CIKIS():
    cevap = QMessageBox.question(MainWindow, "EXIT", "Are you sure you want to sign out?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        conn.close()
        sys.exit(app.exec_())
    else:
        MainWindow.show()


def SIL():
    cevap = QMessageBox.question(MainWindow, "DELETE RECORD", "Are you sure you want to delete the recording?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        secili = ui.tblwBilgi.selectedItems()
        silinecek = secili[1].text()
        try:
            curs.execute("DELETE FROM kitap WHERE Nu='%s'" % (silinecek))
            conn.commit()

            LISTELE()

            ui.statusbar.showMessage("UNREGISTER SUCCESSFUL...", 10000)
        except Exception as Hata:
            ui.statusbar.showMessage("The following error was encountered:" + str(Hata))
    else:
        ui.statusbar.showMessage("Deletion canceled...", 10000)



def KITAPARA():
    adi = ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Adi='%s'" % (adi))
    conn.commit()
    ui.tblwBilgi.clear()
    for row, columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No", 'Number', 'Book Name', 'Author', \
                                            'Publishing House', 'Release Date', 'Type', \
                                            'Shelf Number', 'Shelf Bracket', 'Language', 'Content'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def YAZARARA():
    YazarAdi = ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE YazarAdi='%s'" % (YazarAdi))
    conn.commit()
    ui.tblwBilgi.clear()
    for row, columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No", 'Number', 'Book Name', 'Author', \
                                            'Publishing House', 'Release Date', 'Type', \
                                            'Shelf Number', 'Shelf Bracket', 'Language', 'Content'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def YAYINEVIARA():
    yayinevi = ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Yayinevi='%s'" % (yayinevi))
    conn.commit()
    ui.tblwBilgi.clear()
    for row, columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No", 'Number', 'Book Name', 'Author', \
                                            'Publishing House', 'Release Date', 'Type', \
                                            'Shelf Number', 'Shelf Bracket', 'Language', 'Content'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def TURARA():
    tur = ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Tur='%s'" % (tur))
    conn.commit()
    ui.tblwBilgi.clear()
    for row, columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No", 'Number', 'Book Name', 'Author', \
                                            'Publishing House', 'Release Date', 'Type', \
                                            'Shelf Number', 'Shelf Bracket', 'Language', 'Content'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def DILARA():
    dil = ui.lneAra.text()
    curs.execute("SELECT * FROM kitap WHERE Dil='%s'" % (dil))
    conn.commit()
    ui.tblwBilgi.clear()
    for row, columnvalues in enumerate(curs):
        for column, value in enumerate(columnvalues):
            ui.tblwBilgi.setItem(row, column, QTableWidgetItem(str(value)))
    ui.tblwBilgi.setHorizontalHeaderLabels(("No", 'Number', 'Book Name', 'Author', \
                                            'Publishing House', 'Release Date', 'Type', \
                                            'Shelf Number', 'Shelf Bracket', 'Language', 'Content'))
    ui.tblwBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def DOLDUR():
    secili = ui.tblwBilgi.selectedItems()
    ui.lneNu.setText(secili[1].text())
    ui.lneAdi.setText(secili[2].text())
    ui.lneYazarAdi.setText(secili[3].text())
    ui.lneYayinevi.setText(secili[4].text())
    ui.cmbTarih.setCurrentText(secili[5].text())
    ui.lneTur.setText(secili[6].text())
    ui.spnRaf.setValue(int(secili[7].text()))
    ui.cmbAyrac.setCurrentText(secili[8].text())
    ui.lneDil.setText(secili[9].text())
    ui.lneIcerik.setText(secili[10].text())


def GUNCELLE():
    cevap = QMessageBox.question(MainWindow, "UPDATE RECORD", "Are you sure you want to update the record?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        try:

            secili = ui.tblwBilgi.selectedItems()
            _Id = int(secili[0].text())
            _lneNu = ui.lneNu.text()
            _lneAdi = ui.lneAdi.text()
            _lneYazarAdi = ui.lneYazarAdi.text()
            _lneYayinevi = ui.lneYayinevi.text()
            _cmbTarih = ui.cmbTarih.currentText()
            _lneTur = ui.lneTur.text()
            _spnRaf = ui.spnRaf.value()
            _cmbAyrac = ui.cmbAyrac.currentText()
            _lneDil = ui.lneDil.text()
            _lneIcerik = ui.lneIcerik.toPlainText()

            curs.execute(
                "UPDATE kitap SET Nu=?, Adi=?, YazarAdi=?, Yayinevi=?, Tarih=?, Tur=?, Raf=?, Ayrac=?, Dil=?, Icerik=? WHERE Id=?", \
                (_lneNu, _lneAdi, _lneYazarAdi, _lneYayinevi, _cmbTarih, _lneTur, _spnRaf, _cmbAyrac, _lneDil,
                 _lneIcerik, _Id))
            conn.commit()

            LISTELE()

        except Exception as Hata:
            ui.statusbar.showMessage("An error has occurred:" + str(Hata))
    else:
        ui.statusbar.showMessage("Update canceled", 10000)


ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAd.clicked.connect(KITAPARA)
ui.btnYazar.clicked.connect(YAZARARA)
ui.btnYayinEvi.clicked.connect(YAYINEVIARA)
ui.btnDil.clicked.connect(DILARA)
ui.btnTur.clicked.connect(TURARA)
ui.tblwBilgi.itemSelectionChanged.connect(DOLDUR)
ui.btnGuncelle.clicked.connect(GUNCELLE)
MainWindow.show()

sys.exit(app.exec_())