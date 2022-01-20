a=[]
n=int(input('enter number of elements'))
for i in range (0,n):
    x=int(input("Enter number"))
    a.append(x)
print(a)
val=int(input("Enter value to be searched"))
for j in range (0,len(a)):
 if a[j] == val:
  print(val,'found at location',j+1)
 else :
  print('not found')
  break
