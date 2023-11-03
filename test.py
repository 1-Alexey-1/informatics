#задача2
import os
for adress, dir, name in os.walk(r'\Users\sapfi\informatics'):
    # print(adress)
    for catalog in adress:
            print(f'Папка {catalog[0]} содержит:')
            print(f'Директории:', dir)
#            print(f'Файлы:')
#            print('-' * 40)
    
 
