x=int(input("Nilai x : "))
y=int(input("Nilai y : "))
if x>0 and y>0:
    ket="Positif-Positif"
elif x>0 and y<0:
    ket="Positif-Negatif"
elif x<0 and y>0:
    ket="Negatif-Positif lagi"
elif x<0 and y<0:
    ket="Negatif-Negatif"
else:
    ket="Lain-lain"
print(ket)