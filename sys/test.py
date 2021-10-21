import os, sys
import sqlite3


db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'protocol.db'))
cursor = db.cursor()
var = '00'
cursor.execute("SELECT DESC FROM ERRORS WHERE HEX = '%s'" % var)
result=cursor.fetchone()[0]
print(result)
#print("".join(result[0]))

db.close()
#os.system("pause")
