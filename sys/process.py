#!/usr/bin/env python3
# Файл обработки строк
import os
import sys
import sqlite3
from dict import dict

# Подключение БД
db = sqlite3.connect(':memory:')
reaDb = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
reaDb.backup(db)
reaDb.close()
cursor = db.cursor()


#
# Обработчик строк:
#
def process(line, command):
	if len(line) > 14:  # проверка для обработки пустых строк
	
		# ОБРАБОТЧИКИ КОМАНД ТУТ:
		# 1. Вход в режим
		if line[14:18] == '> 56':
			line = line.rstrip() + " Вход в режим"
			var = line[19:21],
			cursor.execute("SELECT DESC FROM REGIME WHERE HEX = ?", var)
			line = line.rstrip() + cursor.fetchone()[0] + "\n"
				

		# 2. Ответ <55h> <Код ошибки (1)>
		if line[14:18] == '< 55' and len(line) == 26:
			#if command in ("""XX, XX"""):  # Перечень команд, к которым может относиться этот ответ
			if command not in ("""45"""): # Перечень, к которым ответ не применим
				line = line.rstrip() + " Ответ:"
				var = line[19:21],
				cursor.execute("SELECT DESC FROM ERROR WHERE HEX = ?", var)
				line = line.rstrip() + " " + cursor.fetchone()[0] + "\n"
			elif command == "45": # Конкретно к какой комманде применим
				line = line.rstrip() + " В режиме:"
				var = line[19:21],
				cursor.execute("SELECT DESC FROM STATUS_CODE WHERE BIN = ?", var)
				line = line.rstrip() + " " + cursor.fetchone()[0] + "\n"
	
	
	
		#
		# ЗАКОНЧИЛИСЬ ОБРАБОТЧИКИ СТРОК
		#	
		
	return line
#
# FIN
#