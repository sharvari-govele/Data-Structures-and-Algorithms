n=int(input('enter no. of elements'))
a=[int(input('enter no.')) for i in range (n)]
print('unsorted array :',a)
for i in range (0,n):
    for j in range (0,n-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print('Array sorted in ascending order :',a)
for i in range (0,n):
    for j in range (0,n-i-1):
        if a[j]<a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print('Array sorted in descending order :',a)