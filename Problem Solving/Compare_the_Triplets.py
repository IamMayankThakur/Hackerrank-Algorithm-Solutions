ap=0
bp=0
a=list()
b=list()
A = input().split(" ")
B = input().split(" ")
for i in range(0,3):
    a.append(int(A[i]))
    b.append(int(B[i]))
    if(a[i]>b[i]):
        ap+=1
    if(b[i]>a[i]):
        bp+=1
print(ap,bp)