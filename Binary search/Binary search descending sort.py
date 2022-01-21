a=[]
n=int(input('enter number of elements'))
for i in range (0,n):
    x=int(input("Enter number"))
    a.append(x)
print(a)
val=int(input("Enter value to be searched"))
l=0
r=n-1
while(l<=r):
    m=int((l+r)/2)
    if val>a[m]:
      r=m-1
    elif val<a[m]:
      l=m+1
    else :
      print('location is',m+1) 
      break 
if l>r:
    print('no such value found')