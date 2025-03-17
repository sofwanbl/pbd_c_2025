# Buatlah sebuah program untuk mencetak deret bilangan dari a ke b.
# a dan b merupakan bilangan positif. deret dicetak secara horizontal
# Jika terdapat bilangan yanghabis dibagi 4, beri "*" di sebelah angka nya.
# Contoh :
# a : 3
# b : 8
# Output :
# 3 4* 5 6 7 8*
#--------------------------
a=int(input("A:"))
b=int(input("B:"))
print("[", end=" ")
if a>0 and b>0:
   for i in range(a,b+1):
       if i % 4==0:
          print(i,"*", end=" ")
       else:
          print(i,end=" ")
else:
   print("Illegal")
print("]")