from PyQt5 import QtWidgets
import PyQt5
import sys
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
from mainUi import Ui_Form
import sqlite3

# Veritabanı bag.
con = sqlite3.connect("stok.sqlite")
cur = con.cursor()


class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.listele()

    def listele(self):
        con = sqlite3.connect("stok.sqlite")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM defter")
        kayitSayisi = cur.fetchone()
        self.ui.tableWidget.setColumnCount(10)
        self.ui.tableWidget.setRowCount(int(kayitSayisi[0]))

        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(('Urun', 'Kategori', 'Alt Kategori', 'Saklama Koşulu', 'Raf Ömrü',
                                                       'Stok', 'Satış Fiyatı', 'Rezerv', 'Statü', "id"))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        cur.execute("SELECT * FROM defter")
        for satirIndeks, satirVeri in enumerate(cur):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

        self.ui.txt_urun.clear()
        self.ui.txt_kategori.clear()
        self.ui.txt_altKategori.clear()
        self.ui.txt_sk.clear()
        self.ui.txt_ro.clear()
        self.ui.txt_stok.clear()
        self.ui.txt_sf.clear()
        self.ui.txt_rezerv.clear()
        self.ui.txt_statu.clear()

    def ekle(self):
        con = sqlite3.connect("stok.sqlite")
        cur = con.cursor()
        try:

            _lneUrun = self.ui.txt_urun.text()
            _lneKategori = self.ui.txt_kategori.text()
            _lneAltKategori = self.ui.txt_altKategori.text()
            _lneSaklamaKosulu = self.ui.txt_sk.text()
            _lneRafOmru = self.ui.txt_ro.text()
            _lneStok = self.ui.txt_stok.text()
            _lneSatisFiyati = self.ui.txt_sf.text()
            _lneRezerv = self.ui.txt_rezerv.text()
            _lneStatu = self.ui.txt_statu.text()
            _lneid = self.ui.txt_id.text()
            cur.execute("INSERT INTO defter VALUES(?,?,?,?,?,?,?,?,?,?)",
                        (_lneUrun, _lneKategori, _lneAltKategori, _lneSaklamaKosulu, _lneRafOmru, _lneStok,
                         _lneSatisFiyati, _lneRezerv, _lneStatu, _lneid))

        except Exception as Hata:
            print(Hata, "hhhh")
        con.commit()
        con.close()
        self.listele()

    def sil(self):
        secili = self.ui.tableWidget.selectedItems()
        silinecek = secili[9].text()
        try:
            cur.execute("DELETE FROM defter WHERE id='%s'" % (silinecek))
            con.commit()

            self.listele()

        except Exception as hata:
            print(hata)
    def ara(self):

        try:
            adi = self.ui.txt_ara.text()
            cur.execute(f"SELECT * FROM defter WHERE Ürün LIKE'{adi}%'")
            con.commit()
            self.ui.tableWidget.clear()
            for row, columnvalues in enumerate(cur):
                for column, value in enumerate(columnvalues):
                    self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(value)))
            self.ui.tableWidget.setHorizontalHeaderLabels(("Ürün", 'Kategori', 'Alt Kategori', 'Saklama Koşulu',
                                                           'Raf Ömrü', 'Stok', 'Satış Fiyatı', 'Rezerv', 'Statü'))
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as hata:
            print(hata, "urun ara")
    def guncelle(self):
        con = sqlite3.connect("stok.sqlite")
        cur = con.cursor()
        secili = self.ui.tableWidget.selectedItems()
        guncellenecek = secili[9].text()

        _lneUrun = self.ui.txt_urun.text()
        _lneKategori = self.ui.txt_kategori.text()
        _lneAltKategori = self.ui.txt_altKategori.text()
        _lneSaklamaKosulu = self.ui.txt_sk.text()
        _lneRafOmru = self.ui.txt_ro.text()
        _lneStok = self.ui.txt_stok.text()
        _lneSatisFiyati = self.ui.txt_sf.text()
        _lneRezerv = self.ui.txt_rezerv.text()
        _lneStatu = self.ui.txt_statu.text()
        deger=(_lneUrun,_lneKategori,_lneAltKategori,_lneSaklamaKosulu,_lneRafOmru,_lneStok,_lneSatisFiyati,_lneRezerv,_lneStatu,guncellenecek)
        try:
            cur.execute(
                f"UPDATE defter SET Ürün=?,Kategori=?,AltKategori=?,SaklamaKoşulu=?,RafÖmrü=?,Stok=?,SatışFiyatı=?,Rezerv=?,Statü=? WHERE id=?",deger)
            con.commit()
            self.listele()
        except Exception as hata:
            print(hata)


    def fillText(self):
        try:
            secili = self.ui.tableWidget.selectedItems()
            self.ui.txt_urun.setText(secili[0].text())
            self.ui.txt_kategori.setText(secili[1].text())
            self.ui.txt_altKategori.setText(secili[2].text())
            self.ui.txt_sk.setText(secili[3].text())
            self.ui.txt_ro.setText(secili[4].text())
            self.ui.txt_stok.setText(secili[5].text())
            self.ui.txt_sf.setText(secili[6].text())
            self.ui.txt_rezerv.setText(secili[7].text())
            self.ui.txt_statu.setText(secili[8].text())

        except Exception as hata:
            print(hata)


    def callBackButton(self):
        con = sqlite3.connect("stok.sqlite")
        cur = con.cursor()
        content = 'SELECT * FROM defter'
        res = cur.execute(content)
        for row in enumerate(res):
            if row[0] == self.ui.tableWidget.currentRow():
                data = row[1]
                curun = data[0]
                ckategori = data[1]
                caltKategori = data[2]
                csaklamaKosulu = data[3]
                crafOmru = data[4]
                cstok = data[5]
                csatisFiyati = data[6]
                crezerv = data[7]
                cstatu = data[8]

        return self.guncelle(curun)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()

    win.ui.btn_listeGetir.clicked.connect(win.listele)
    win.ui.tableWidget.itemSelectionChanged.connect(win.fillText)
    win.ui.btn_ekle.clicked.connect(win.ekle)
    win.ui.btn_sil.clicked.connect(win.sil)
    win.ui.btn_guncelle.clicked.connect(win.guncelle)
    win.ui.btn_ara.clicked.connect(win.ara)
    sys.exit(app.exec_())


app()
