'''
# номер1 Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». Преобразовать её,
# заменив точками все восклицательные знаки
s=input('введите строку ')
s+=' '
m=0
k=0
for i in range(len(s)):
    if s[i]=='н':
        k+=1
    elif k>m:
        m=k
        k=0
z=s.replace('!','.')
print(z)
print(m)
'''
'''
#номер2 Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. Вывести на экран все символы,
#расположенные внутри этих скобок.
s=input('введите строку ')
m=(s.index('(')+1)
k=s.index(')')
a=s[m:k]
print(a)
'''
'''
#номер3 Дана строка. Вывести все слова, начинающиеся на букву "а" и слова оканчивающиеся на букву "я". Например: Абстракция, авария, аллея.
s=input('введите сторку ')
for i in s.split(' '):
    if(i.startswith('а')) or (i.endswith('я')):
        print(i)
'''