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


errorCommand = "+== Команда не известна или ошибка обработки строки +==\n"
errorSubCommand = "=+= Подкомманда не известна или ошибка обработки строки =+=\n"


#
# Обработчик строк:
#
def process(line, command):
	if len(line) > 14:  # проверка для обработки пустых строк
	
		# 
		# ОБРАБОТЧИКИ КОМАНД:
		if line[14:16] == '> ':
		#
		

			if command == '56':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM REGIME WHERE HEX = ?", hex_2)				
					line = " ".join([line.rstrip(), "Вход в режим", cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorSubCommand])

			
			elif command == 'A4':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'A4' AND HEX_2 = ?", hex_2)					
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorSubCommand])

			
			elif command == 'EF':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EF' AND HEX_2 = ?", hex_2)				
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorSubCommand])

					
			elif command == 'CE':
				
				if line[19:21] == "41":
					line = " ".join([line.strip(), "Перезагрузка ККТ\n"])
				else:	
					line = " ".join([line.strip(), "Выключение\n"])

					
			elif command == 'EC':
				if line[19:21] == '0A':
					if line[23:25] == '01':
						line = " ".join([line.strip(), "Восстановление необнуляемой суммы, Приход\n"])
					elif line[23:25] == '02':
						line = " ".join([line.strip(), "Восстановление необнуляемой суммы, Возврат прихода\n"])
					elif line[23:25] == '04':
						line = " ".join([line.strip(), "Восстановление необнуляемой суммы Расход\n"])
					elif line[23:25] == '05':
						line = " ".join([line.strip(), "Восстановление необнуляемой суммы Возврат расхода\n"])
					else:
						line = " ".join([line.strip(), "Запись в таблицу настроек ФР"])
				elif line[19:21] == '0B':
					line = " ".join([line.strip(), "Чтение таблицы настроек ФР"])
				else:
					try:
						hex_2 = line[19:21],
						cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EC' AND HEX_2 = ?", hex_2)
						line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
					except:
						line = " ".join([line.rstrip(), errorCommand])

			
			elif command == 'ED':
				if len(line) == 23:
					try:
						hex_2 = line[19:21],
						cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'ED' AND HEX_2 = ?", hex_2)
						line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
					except:
						line = " ".join([line.rstrip(), errorCommand])
				else:
					line = " ".join([line.strip(), "Программирование даты и времени\n"])


			#  Обработка всех остальных комманд, которые не были перечислены выше.
			else:
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = ?", (command,))
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorCommand])
					

			
		# 
		# ОБРАБОТЧИКИ ОТВЕТОВ:
		if line[14:16] == '< ':
		#
		
			# 1. Ответ <55h> <Код ошибки (1)>
			if line[16:18] == '55' and len(line) == 26:
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
	
	
	
		#
		# ЗАКОНЧИЛИСЬ ОБРАБОТЧИКИ СТРОК
		#	
		
	return line
#
# FIN
#
