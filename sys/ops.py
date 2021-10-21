#!/usr/bin/env python3
# Файл обработки строк
import os
import sys
import sqlite3
from dict import dict

# Подключение БД
db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'protocol.db'))
cursor = db.cursor()


#
# Обработчик строк:
#
def linewrapper(line):
	if len(line) > 14:  # проверка для обработки пустых строк
	
		#
		# ОБРАБОТЧИКИ КОМАНД ТУТ:
		#
		
		# 1. Вход в режим
		if line[14:18] == '> 56':
			line = line.rstrip() + " Вход в режим"
			if line[19:21] == '00':
				line = line.rstrip() + " выбора\n"
			if line[19:21] == '01':
				line = line.rstrip() + " регистрации\n"
			if line[19:21] == '02':
				line = line.rstrip() + " отчетов без гашения\n"
			if line[19:21] == '03':
				line = line.rstrip() + " отчетов с гашением\n"
			if line[19:21] == '04':
				line = line.rstrip() + " программирования\n"
			if line[19:21] == '05':
				line = line.rstrip() + " ввода ЗН\n"
			if line[19:21] == '06':
				line = line.rstrip() + " доступа к ФН\n"	
		
		# 2. Ответ
		if line[14:18] == '< 55':
			#line = line.rstrip() + " Ответ:"
			var = line[19:21]
			cursor.execute("SELECT DESC FROM ERRORS WHERE HEX = '%s'" % var)
			line = line.rstrip() + " " + cursor.fetchone()[0] + "\n"
	
	
	
		#
		# ЗАКОНЧИЛИСЬ ОБРАБОТЧИКИ СТРОК
		#	
		
	return line
#
# FIN
#