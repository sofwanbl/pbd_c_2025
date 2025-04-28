# Searching berdasarkan Alamat
import pymysql
dbku=pymysql.connect(host="localhost",user="root",
                     password="opansan123",database="test")
kursor=dbku.cursor()
alamat=input("Alamat :")

# Cari data mahasiswa
cari="select * from master_mhs where alamat like '%"+ alamat +"%' "
kursor.execute(cari)
hasil=kursor.fetchall()

if (kursor.rowcount)>0:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

