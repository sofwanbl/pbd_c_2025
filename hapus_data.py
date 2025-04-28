import pymysql
dbku=pymysql.connect(host="localhost",user="root",
                     password="opansan123",database="test")
kursor=dbku.cursor()
nama_depan=input("Nama Depan :")
alamat=input("Alamat :")

# Cari data mahasiswa
cari="select npm from master_mhs where nama like '"+ nama_depan +"%' and  alamat like '%"+alamat+"%' "
kursor.execute(cari)
hasil=kursor.fetchall()
jumlah=kursor.rowcount

if len(hasil)>0:
    # Hapus data mahasiswa
    hapus = "delete from master_mhs where nama like '"+ nama_depan +"%' and  alamat like '%"+ alamat +"%'"
    kursor.execute(hapus)
    dbku.commit()
    print(jumlah ," baris data berhasil dihapus")
else:
    print("Tidak ada data yang dihapus")