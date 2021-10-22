import os, sys
import sqlite3

print(len("12:22:21.024 << 55 00 00 "))








'''
Подключение к БД

db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
cursor = db.cursor()
var = '00'
cursor.execute("SELECT DESC FROM ERRORS WHERE HEX = '%s'" % var)
result=cursor.fetchone()[0]
print(result)
#print("".join(result[0]))

db.close()
#os.system("pause")
'''


'''
sys.byteorder - порядок байтов. Будет иметь значение 'big' при порядке следования битов от старшего к младшему, и 'little', если наоборот (младший байт первый).


'''
