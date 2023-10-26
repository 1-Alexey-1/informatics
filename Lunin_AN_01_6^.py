'''
#задание1 Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива;
#максимальное значение среди элементов второй строки массива. Вывести полученные значения.
a=int(input('введите размер массива: '))
mas=[]
for g in range(a):
    mas.append(list(map(int,input().split())))
m=mas[0][2]
m2=mas[1][0]
for i in range(a):
    for j in range(a):
        if mas[1][j]>m2:
            m2=mas[1][j]
        if mas[i][2]>m:
            m=mas[i][2]
print(m, m2)
'''
'''
#задание2 Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами,
#а отрицательные нулями. Вывести оба массива.
m=int(input('введите количество m столбцов массива:'))
n=int(input('введите количество n строк массива:'))
mas=[]
arr=[]
for g in range(n):
    mas.append(list(map(int,input().split())))
print()
arr=mas.copy()
for i in range(n):
    for j in range(m):
        print(mas[i][j], end = ' ')
    print()
print()
for i in range(n):
    for j in range(m):
        if arr[i][j]<0:
            arr[i][j]=0
        if arr[i][j]>0:
            arr[i][j]=1
        print(arr[i][j], end = ' ')
    print()
'''
'''
#задание3 Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом,
#т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
a=int(input('введите размер массива: '))
mas=[]
flag=1
for g in range(a):
    mas.append(list(map(int,input().split())))
f=sum(mas[0])
for c in range(1,a):
    if sum(mas[0])!=f:
        flag=0
for c in range(a):
    if sum([g[c] for g in mas])!=f:
        flag=0
if flag==1:
    print('это магический квадрат')
else: print('это не магический квадрат')
'''
'''
#задание4 Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
a=int(input('введите размер массива: '))
mas=[]
k=1
for g in range(a):
    mas.append(list(map(int,input().split())))
for i in range(a-1):
    for j in range(i+1,a):
        if mas[i][j]!=mas[j][i]:
            k=0
            break
if k!=0:
    print('Матрица симметрична')
else:
    print('Обычная матрица')
'''