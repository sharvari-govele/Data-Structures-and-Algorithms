n=int(input('enter no. of rows '))
m=int(input('enter no. of columns '))
a=[[int(input('enter rows of first matrix')) for i in range (n)]for j in range (m)]
print(a)
b=[[int(input('enter rows of second matrix')) for i in range (n)]for j in range (m)]
print(b)
z=[[0]*n]*m
def add(x,y):
    for i in range (n):
        for j in range (m):       
            z[i][j]=x[i][j]+y[i][j]
add(a,b)
print(z)