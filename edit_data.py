import pymysql
dbku=pymysql.connect(host="localhost",user="root",
                     password="opansan123",database="test")
kursor=dbku.cursor()
nama_depan=input("Nama Depan :")
alamat=input("Alamat :")

# Cari data mahasiswa
cari="select npm from master_mhs where nama like '" + nama_depan +"%'"
kursor.execute(cari)
hasil=kursor.fetchall()
jumlah=kursor.rowcount

if len(hasil)>0:
    # Hapus data mahasiswa
    edit = "update master_mhs set alamat='"+alamat+"' where nama like '"+ nama_depan +"%'"
    kursor.execute(edit)
    dbku.commit()
    print(jumlah ," baris data berhasil diedit")
else:
    print("Tidak ada data yang diedit")