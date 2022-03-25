import pandas as pd
import csv, sqlite3
import pandas as pd
import numpy as np

con = sqlite3.connect("stok.sqlite")
cur = con.cursor()
cur.execute(
    "CREATE TABLE defter (Ürün,Kategori,AltKategori,SaklamaKoşulu,RafÖmrü,Stok,SatışFiyatı,Rezerv,Statü)")
a_file = open("stok.csv", encoding='UTF-8')
rows = csv.reader(a_file)
try:
    cur.executemany(f"INSERT INTO defter VALUES (?,?,?,?,?,?,?,?,?)", rows)
except Exception as Hata:
    print(Hata, "hhhh")

con.commit()
con.close()
