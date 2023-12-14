'''
#Задание1 Создать объект pandas Series из листа, объекта NumPy, и словаря
import numpy as np
import pandas as pd
s_list = list('abcde')
s_arr = np.arange(5)
s_dict = dict(zip(s_list, s_arr))
 
s1 = pd.Series(s_list)
s2 = pd.Series(s_arr)
s3 = pd.Series(s_dict)
 
print(s1)
print(s2)
print(s3)
'''
'''
#Задание2 Получить не пересекающиеся элементы в двух объектах Series
import pandas as pd
import numpy as np
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
a=pd.Series(np.setxor1d(s1, s2))
print(a)
'''
'''
#Задание3 Узнать частоту уникальных элементов объекта Series (гистограмма)
import numpy as np
import pandas as pd
lst = np.random.randint(1, 5, 10)
print(*lst)
s1 = pd.Series(lst)
a = s1.value_counts()
print(a)
'''
'''
#задание4 Объединить два объекта Series вертикально и горизонтально
import pandas as pd
s1 = pd.Series(range(5))
s2 = pd.Series([6,7,8,9,10])
vert = pd.concat([s1, s2])
hor = pd.concat([s1, s2], axis=1)
print(vert)
print(hor)
'''
'''
#задание5 Найти разность между объектом Series и смещением объекта Series на n
import pandas as pd
n=int(input('введите n: '))
s=pd.Series([1, 1, 2, 7, 4, 14, 20])
a=s.diff(n)
print(a)
'''