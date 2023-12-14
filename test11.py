import numpy as np
import pandas as pd
src_list = list('abcde')
src_arr = np.arange(5)
src_dict = dict(zip(src_list, src_arr))
 
s1 = pd.Series(src_list)
s2 = pd.Series(src_arr)
s3 = pd.Series(src_dict)
 
print(s1)
print(s2)
print(s3)