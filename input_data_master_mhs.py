#Load dan konek Library pymysql
import pymysql
dbku=pymysql.connect(host="localhost",user="root",password="opansan123",
                     database="test")
kursor=dbku.cursor()
npm=input("NPM:")
nama=input("Nama:")
alamat=input("Alamat:")

sql="insert into master_mhs (npm,nama,alamat) values (%s,%s,%s)"
val=(npm,nama,alamat)

kursor.execute(sql,val)
dbku.commit()
print(kursor.rowcount," row inserted")