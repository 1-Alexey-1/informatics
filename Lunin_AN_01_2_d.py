from random import randint
c=int(input('введите длину массива '))
a=[]
for i in range(c):
    n=randint(-100,100)
    a.append(n)
print(a)
p=0
while p<c:
    if a[p]<0:
        del a[p]
        c-=1
    else:
        p+=1
print(a)