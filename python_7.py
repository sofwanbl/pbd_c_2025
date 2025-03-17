a=int(input("Nilai a:"))
b=int(input("Nilai b:"))
for i in range(a,b+1):
    if i % 2==0:
      print(i,"(Genap)",end=" ")
    else:
      print(i,end=" ")