#!/usr/bin/env python3
# Файл обработки строк
import os
import sys
import sqlite3


errorCommand = "+=== Команда не известна или ошибка обработки строки. Проверьте обновление программы"
errorSubCommand = "=+== Подкомманда не известна или ошибка обработки строки. Проверьте обновление программы"
errorTag = "(описание отсутствует, проверьте обновление программы) ==+="


# Подключение БД
db = sqlite3.connect(':memory:')
reaDb = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
reaDb.backup(db)
reaDb.close()
cursor = db.cursor()

#
# Обработчик строк:
#
def process(line, command, subCommand):
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
					line = " ".join([line.rstrip(), errorSubCommand, "\n"])

			
			elif command == 'A4':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'A4' AND HEX_2 = ?", hex_2)					
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorSubCommand, "\n"])

			
			elif command == 'EF':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EF' AND HEX_2 = ?", hex_2)				
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorSubCommand, "\n"])

					
			elif command == 'CE':
				
				if line[19:21] == "41":
					line = " ".join([line.strip(), "Перезагрузка ККТ\n"])
				else:	
					line = " ".join([line.strip(), "Выключение\n"])

					
			elif command == 'EC':
				if line[19:21] == '0A':
					if line[22:24] == '28':
						hex_3 = line[25:27],
						try:
							cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EC' AND HEX_2 = '0A' AND HEX_3 = ?", hex_3)				
							line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
						except:
							line = " ".join([line.rstrip(), errorSubCommand, "\n"])
					else:
						line = " ".join([line.strip(), "Запись в таблицу настроек ФР \n"])
				elif line[19:21] == '0B':
					line = " ".join([line.strip(), "Чтение таблицы настроек ФР \n"])
				else:
					try: #  Обновление ФР.
						hex_2 = line[19:21],
						cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EC' AND HEX_2 = ?", hex_2)
						line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
					except:
						line = " ".join([line.rstrip(), errorCommand, "\n"])

			
			elif command == 'ED':
				if len(line) == 23:
					try:
						hex_2 = line[19:21],
						cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'ED' AND HEX_2 = ?", hex_2)
						line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
					except:
						line = " ".join([line.rstrip(), errorCommand, "\n"])
				else:
					line = " ".join([line.strip(), "Программирование даты и времени \n"])


			elif command == '91':
				line = " ".join([line.rstrip(), "Считать регистр", str(int(line[19:21], 16)), "\n"])
				
			elif command == '82':
					try:
						hex_3 = line[23],
						cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = '82' AND HEX_3 = ?", hex_3)
						line = " ".join([line.rstrip(), "Демонстрационная печать:", cursor.fetchone()[0], "\n"])
					except:
						line = " ".join([line.rstrip(), "Демонстрационная печать:", errorSubCommand, "\n"])
				
				# Расшифровка легенды запроса из Протокола. Не соответствует Эвотору и загрязняет результат визуально.
				# try:
					# hex_2 = line[19:21],
					# cursor.execute("SELECT DESC FROM REGISTER WHERE HEX_2 = ?", hex_2)
					# line = " ".join([line.rstrip(), "Считать регистр", str(int(line[19:21], 16)), cursor.fetchone()[0], "\n"])
				# except:
					# line = " ".join([line.rstrip(), "Считать регистр", str(int(line[19:21], 16)), errorSubCommand, "\n"])
				
				
			elif command == 'E8':
				valueBlockNumber = int(line[25:27], 16)
				if valueBlockNumber == 0:			
					try:	
						hex_btswpt = line[28:33],
						cursor.execute("SELECT TAG, NAME FROM TAGS WHERE HEX_BYTESWAPPED = ?", hex_btswpt)
						tagAndName = cursor.fetchone()
						line = "".join([line.rstrip(), " Запись реквизита ", tagAndName[0], " \"", tagAndName[1], "\"", " \n"])
					except:
						tagSwypedBack = str(int("".join([line[31:33], line[28:30]]), 16))
						line = " ".join([line.rstrip(), "Запись реквизита", tagSwypedBack, errorTag, "\n"])
				else:
					line = " ".join([line.rstrip(), "продолжение записи реквизита, блок", str(valueBlockNumber + 1), "\n"])


			elif command == 'E9':
				try:	
					hex_btswpt = line[19:24],
					cursor.execute("SELECT TAG, NAME FROM TAGS WHERE HEX_BYTESWAPPED = ?", hex_btswpt)
					tagAndName = cursor.fetchone()
					line = "".join([line.rstrip(), " Чтение реквизита ", tagAndName[0], " \"", tagAndName[1], "\"", " \n"])
				except:
					tagSwypedBack = str(int("".join([line[22:24], line[19:21]]), 16))
					line = " ".join([line.rstrip(), "Чтение реквизита", tagSwypedBack, errorTag, "\n"])


			#
			#  Обработка всех остальных комманд, которые не были перечислены выше.
			#
			else:
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = ?", (command,))
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), errorCommand, "\n"])
					

			
		# 
		# ОБРАБОТЧИКИ ОТВЕТОВ:
		if line[14:16] == '< ':
		#
			answer = line[16:18]

			# Костыль по регистру 55
			if command == '91':
				if subCommand == '37':
					if line[25:27] == 'EC':
						try:
							error_55 = line[28:30],
							cursor.execute("SELECT DESC FROM REGISTER_55 WHERE ANSWER = ?", error_55)
							line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
							if line[28:30] == '04':
								try:
									fw_err = line[31:33],
									cursor.execute("SELECT DESC FROM REGISTER_55_FW_ERR WHERE ERR = ?", fw_err)
									line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
								except:
									line = " ".join([line.rstrip(), "Не удалось определить: передайте автору программы, что нужно исправить чтение бинарной маски ===+", "\n"])
						except:
							line = " ".join([line.rstrip(), "Неизвестная ошибка обновления (проверьте обновление программы) ===+ \n"])



			# <55h> <Код ошибки (2)>
			elif answer == '55' and len(line) == 26:  # <-- только для ответов длиной 26 !
				#if command in ("""XX, XX"""):  # Перечень команд, к которым может относиться этот ответ
				if command not in ("""45"""): # Перечень, к которым ответ не применим
					line = " ".join([line.rstrip(), "Ответ:"])
					var = line[19:21],
					cursor.execute("SELECT DESC FROM ERROR WHERE HEX = ?", var)
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				elif command == "45": # Конкретно к какой комманде применим
					line = " ".join([line.rstrip(), "В режиме:"])
					var = line[19:21],
					cursor.execute("SELECT DESC FROM STATUS_CODE WHERE BIN = ?", var)
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
		
						
	
	

		# ЗАКОНЧИЛИСЬ ОБРАБОТЧИКИ СТРОК
		
	return line
#
# FIN
#
