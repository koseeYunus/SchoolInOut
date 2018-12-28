# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


vt= sqlite3.connect("ziyaretciler.db")
im= vt.cursor()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("background-color: #307D7E")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.tcuyari = QtWidgets.QMessageBox()
        self.tcuyari.setIcon(QtWidgets.QMessageBox.Warning)
        self.tcuyari.setInformativeText("Lütfen T.C no doğru şekilde giriniz.")
        self.tcuyari.setWindowTitle("Uyarı")
        self.tcuyari.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.secimuyari = QtWidgets.QMessageBox()
        self.secimuyari.setIcon(QtWidgets.QMessageBox.Warning)
        self.secimuyari.setInformativeText("Önce çıkış yapacak ziyaretçiyi seçiniz.")
        self.secimuyari.setWindowTitle("Uyarı")
        self.secimuyari.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.cikanlar = QtWidgets.QTableWidget(self.centralwidget)
        self.cikanlar.setGeometry(QtCore.QRect(390, 350, 480, 250))
        self.cikanlar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cikanlar.setRowCount(0)
        self.cikanlar.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setText("T.C NO")
        self.cikanlar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("GİRİŞ")
        self.cikanlar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("ÇIKIŞ")
        self.cikanlar.setHorizontalHeaderItem(1, item)
        self.cikanlar.horizontalHeader().setVisible(True)
        self.cikanlar.horizontalHeader().setCascadingSectionResizes(True)
        self.cikanlar.horizontalHeader().setHighlightSections(False)
        self.cikanlar.horizontalHeader().setSortIndicatorShown(False)
        self.cikanlar.verticalHeader().setVisible(False)
        self.cikanlar.verticalHeader().setHighlightSections(False)
        self.cikanlar.verticalHeader().setMinimumSectionSize(15)
        self.cikanlar.horizontalHeader().setVisible(True)
        self.cikanlar.horizontalHeader().setCascadingSectionResizes(True)
        self.cikanlar.horizontalHeader().setHighlightSections(False)
        self.cikanlar.verticalHeader().setVisible(False)
        self.cikanlar.verticalHeader().setHighlightSections(False)
        self.cikanlar.verticalHeader().setMinimumSectionSize(15)
        self.cikanlar.setDragDropOverwriteMode(False)
        self.cikanlar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cikanlar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.cikanlar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cikanlar.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cikanlar.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cikanlar.setShowGrid(True)
        self.cikanlar.setGridStyle(QtCore.Qt.SolidLine)
        self.cikanlar.setWordWrap(True)
        self.cikisyap = QtWidgets.QPushButton(self.centralwidget)
        self.cikisyap.setGeometry(QtCore.QRect(760, 280, 100, 23))
        self.cikisyap.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.girisyap = QtWidgets.QPushButton(self.centralwidget)
        self.girisyap.setGeometry(QtCore.QRect(135, 350, 100, 23))
        self.girisyap.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.girenler = QtWidgets.QTableWidget(self.centralwidget)
        self.girenler.setGeometry(QtCore.QRect(390, 60, 480, 210))
        self.girenler.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.girenler.setColumnCount(3)
        self.girenler.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("T.C NO")
        self.girenler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("İSİM")
        self.girenler.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("GİRİŞ")
        self.girenler.setHorizontalHeaderItem(2, item)
        self.girenler.horizontalHeader().setVisible(True)
        self.girenler.horizontalHeader().setCascadingSectionResizes(True)
        self.girenler.horizontalHeader().setHighlightSections(False)
        self.girenler.verticalHeader().setVisible(False)
        self.girenler.verticalHeader().setHighlightSections(False)
        self.girenler.verticalHeader().setMinimumSectionSize(15)
        self.girenler.setDragDropOverwriteMode(False)
        self.girenler.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.girenler.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.girenler.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.girenler.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.girenler.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.girenler.setShowGrid(True)
        self.girenler.setGridStyle(QtCore.Qt.SolidLine)
        self.girenler.setWordWrap(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 330, 480, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(211, 255, 250);")
        self.label.setText(" ÇIKIŞ YAPANLAR")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(390, 40, 480, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("background-color: rgb(211, 255, 250);")
        self.label1.setText("GİRİŞ YAPANLAR")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 211, 281))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 120, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(211, 255, 247);")
        self.label_5.setText("   TC")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(0, 65, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(211, 255, 247);")
        self.label_6.setText("   SOYAD")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 7, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(211, 255, 247);")
        self.label_7.setText("   AD")
        self.ad = QtWidgets.QLineEdit(self.widget)
        self.ad.setGeometry(QtCore.QRect(12, 32, 141, 20))
        self.ad.setText("")
        self.soyad = QtWidgets.QLineEdit(self.widget)
        self.soyad.setGeometry(QtCore.QRect(12, 90, 141, 20))
        self.soyad.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.soyad.setText("")
        self.tc = QtWidgets.QLineEdit(self.widget)
        self.tc.setGeometry(QtCore.QRect(12, 145, 141, 20))
        self.tc.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tc.setText("")
        self.tc.setInputMask("99999999999")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(0, 174, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(211, 255, 247);")
        self.label_8.setText("   ZİYARET SEBEBİ")
        self.ziyaretsebep = QtWidgets.QTextEdit(self.widget)
        self.ziyaretsebep.setGeometry(QtCore.QRect(12, 203, 191, 61))
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        def ziyaretci_cikis():
            saat = datetime.now().strftime('%H:%M')
            secim = self.girenler.currentRow()
            try:
                im.execute("UPDATE ziyaretciler SET durum = 0 , cikis = ? WHERE no LIKE ?",[saat,ziyaretciler[secim][4]])
                vt.commit()
                girenlerfonk()
                cikanlarfonk()
            except:
                self.secimuyari.exec_()
        def temizliste():
            self.ad.setText("")
            self.soyad.setText("")
            self.tc.setText("")
            self.ziyaretsebep.setText("")
            self.horizontalLayout.addWidget(self.widget)
        def girenlerfonk():
            icerde = 1
            im.execute("SELECT tc,ad,giris,soyad,no FROM ziyaretciler WHERE durum LIKE ? AND tarih LIKE ? ",[icerde,str(tarih)])
            global ziyaretciler
            ziyaretciler = im.fetchall()
            if len(ziyaretciler) != 0:
                row = len(ziyaretciler)
                self.girenler.setColumnCount(3)
                self.girenler.setRowCount(row)
                for i in range(0,row):
                    isim  = ziyaretciler[i][1] + " " + ziyaretciler[i][3]
                    for k in range(0,3):
                        if k == 1:
                            item = QtWidgets.QTableWidgetItem()
                            item.setText(isim)
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            item.setFlags(
                                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                            self.girenler.setItem(i, k, item)
                        else:
                            item = QtWidgets.QTableWidgetItem()
                            text = str(ziyaretciler[i][k])
                            item.setText(text)
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            item.setFlags(
                                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                            self.girenler.setItem(i, k, item)
                self.girenler.scrollToBottom()
        def cikanlarfonk():
            im.execute("SELECT giris,cikis,tc FROM ziyaretciler WHERE durum = 0 ")
            cknlr= im.fetchall()
            if len(cknlr) != 0:
                row1=len(cknlr)
                self.cikanlar.setColumnCount(3)
                self.cikanlar.setRowCount(row1)
                for i in range(0,row1):
                    for k in range(0,3):
                        item = QtWidgets.QTableWidgetItem()
                        text = str(cknlr[i][k])
                        item.setText(text)
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFlags(
                            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        self.cikanlar.setItem(i, k, item)
                self.cikanlar.scrollToBottom()

        tarih = datetime.now().strftime('%Y-%m-%d')
        girenlerfonk()
        cikanlarfonk()
        def ziyaretci_kayit():
            saat = datetime.now().strftime('%H:%M')
            veri=["","","",""]
            veri[0] = self.ad.text()
            veri[1] = self.soyad.text()
            try:
                a = b = ilk_on = 0
                veri[2] = int(self.tc.text())
                veri[3] = self.ziyaretsebep.toPlainText()
                tc_no=str(self.tc.text())
                if len(tc_no) != 11:
                    self.tcuyari.exec_()
                elif tc_no[0] != "-":
                    for i in range(0, 10, 2): a += int(tc_no[i])
                    for i in range(1, 9, 2): b += int(tc_no[i])
                    for i in range(0, 10, 1): ilk_on += int(tc_no[i])
                    if int((a * 7 - b) % 10) != (int(tc_no[9])):
                        self.tcuyari.exec_()
                    elif int(ilk_on % 10) != (int(tc_no[10])):
                        self.tcuyari.exec_()
                    else:
                        icerde = 1
                        im.execute(
                            "INSERT INTO ziyaretciler (tarih,giris,ad,soyad,tc,sebep,durum) VALUES (?,?,?,?,?,?,?)",
                            [tarih, saat, veri[0], veri[1], veri[2], veri[3], icerde])
                        vt.commit()
                        try:
                            self.horizontalLayout.removeWidget(self.widget)
                        except:
                            pass
                        temizliste()
                        girenlerfonk()
                else:
                    self.horizontalLayout.removeWidget(self.widget)
            except:
                self.tcuyari.exec_()
        self.girisyap.clicked.connect(ziyaretci_kayit)
        self.cikisyap.clicked.connect(ziyaretci_cikis)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ziyaretçi Kayıt Programı"))
        self.cikisyap.setText(_translate("MainWindow", "ÇIKIŞ YAP"))
        self.girisyap.setText(_translate("MainWindow", "GİRİŞ YAP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

