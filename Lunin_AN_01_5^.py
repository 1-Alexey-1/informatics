'''
#задание1 три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). Найти и напечатать координаты точки,
#для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. Вычисления оформить в виде процедуры.
import math
def k(x,y):
    p=math.degrees(math.atan(abs(y/x)))
    return p
def g(f,h,j):
    a=min(f, h, j)
    if a==f:
        print(x1,x2)
    elif a==h:
        print(y1, y2)
    else: print(z1,z2)
x1,x2=map(int,input('введите координаты 1: ').split())
y1,y2=map(int,input('введите координаты 2: ').split())
z1,z2=map(int,input('введите координаты 3: ').split())
g(k(x1,x2), k(y1,y2), k(z1, z2))
'''
'''
#задвние2 Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром,
#т. е. читается одинаково слева направо и справа налево.
n=int(input('введите n '))
def p(t):
    k=0
    for j in range(2, t//2+1):
        if(t%j==0):
            k=k+1
    if (k<=0):
        return 1
    else:
        return 0
def f(c):
    return c==c[::-1]
def k(n):
    for i in range(2,n):
        if p(i)==1:
            a=str(bin(i))
            a=a[2:]
            if f(a)==True:
                print(i)
k(n)
'''
