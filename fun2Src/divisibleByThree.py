n= int (input())
s=0
br=0
for i  in range (n,n+n):
     if i%3==0:
         print("Brojevi djeljivi sa tri su: ", i)
         s=s+i
         br=br+1
ars=s/br
print ("artmeticka vrijednost je: ",ars)
