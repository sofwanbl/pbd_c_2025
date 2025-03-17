nilai_1=int(input("Nilai 1 :"))
nilai_2=int(input("Nilai 2 :"))
jumlah=nilai_1+nilai_2
if jumlah>100 and nilai_1>20 and nilai_2>20:
    ket="Golongan 1"
elif jumlah>=50 and jumlah<100 and nilai_2>20:
    ket="Golongan 2"
else:
    ket="Golongan 3"
print(ket)