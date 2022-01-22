n=int(input('enter no. of elements'))
a=[int(input('enter no.')) for i in range (n)]
print('unsorted array :',a)
for i in range (0,n):
    for j in range (i+1,n):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print('Array sorted in ascending order :',a)
for i in range (0,n):
    for j in range (i+1,n):
        if a[i]<a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print('Array sorted in descending order :',a)