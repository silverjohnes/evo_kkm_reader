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
					line = " ".join([line.rstrip(), "=== Ошибка обработки строки ===\n"])
			
			elif command == 'A4':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'A4' AND HEX_2 = ?", hex_2)					
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), "=== Ошибка обработки строки ===\n"])
			
			elif command == 'EF':
				hex_2 = line[19:21],
				try:
					cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EF' AND HEX_2 = ?", hex_2)				
					line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
				except:
					line = " ".join([line.rstrip(), "=== Ошибка обработки строки ===\n"])
					
				
			if command == '3F':
				line = " ".join([line.strip(), "Запрос состояния ККТ\n"])
			
			
			if command == '43':
				line = " ".join([line.strip(), "Скидка\n"])
			
			
			if command == '45':
				line = " ".join([line.strip(), "Запрос кода состояния ККТ\n"])
			
			
			if command == '46':
				line = " ".join([line.strip(), "Чтение таблицы\n"])
			
			
			if command == '47':
				line = " ".join([line.strip(), "Гудок\n"])
			
			
			if command == '48':
				line = " ".join([line.strip(), "Выход из текущего режима\n"])
			
			
			if command == '49':
				line = " ".join([line.strip(), "Внесение денег\n"])
			
			
			if command == '4A':
				line = " ".join([line.strip(), "Закрыть чек (со сдачей)\n"])
			
			
			if command == '4B':
				line = " ".join([line.strip(), "Программирование времени\n"])
			
			
			if command == '4C':
				line = " ".join([line.strip(), "Печать строки\n"])
			
			
			if command == '4D':
				line = " ".join([line.strip(), "Запрос наличных\n"])
			
			
			if command == '4F':
				line = " ".join([line.strip(), "Выплата денег\n"])
			
			
			if command == '50':
				line = " ".join([line.strip(), "Программирование таблицы\n"])
			
			
			if command == '58':
				line = " ".join([line.strip(), "Получение последнего сменного итога\n"])
			
			
			if command == '59':
				line = " ".join([line.strip(), "Аннулирование всего чека\n"])
			
			
			if command == '5A':
				line = " ".join([line.strip(), "Снятие суточного отчета с гашением (закрытие смены)\n"])
			
			
			if command == '61':
				line = " ".join([line.strip(), "Ввод заводского номера\n"])
			
			
			if command == '62':
				line = " ".join([line.strip(), "Активизация памяти ПД\n"])
			
			
			if command == '64':
				line = " ".join([line.strip(), "Программирование даты\n"])
			
			
			if command == '65':
				line = " ".join([line.strip(), "Отчет ППД по диапазону дат\n"])
			
			
			if command == '66':
				line = " ".join([line.strip(), "Отчет ППД по диапазону смен\n"])
			
			
			if command == '67':
				line = " ".join([line.strip(), "Начало снятия отчета без гашения\n"])
			
			
			if command == '6B':
				line = " ".join([line.strip(), "Технологическое обнуление ККТ\n"])
			
			
			if command == '6C':
				line = " ".join([line.strip(), "Печать клише чека\n"])
			
			
			if command == '6D':
				line = " ".join([line.strip(), "Ввод кода защиты ККТ\n"])
			
			
			if command == '71':
				line = " ".join([line.strip(), "Инициализация таблиц нач. значениями\n"])
			
			
			if command == '73':
				line = " ".join([line.strip(), "Печать нижней части чека\n"])
			
			
			if command == '74':
				line = " ".join([line.strip(), "Запрос активизированности кода защиты ККТ\n"])
			
			
			if command == '75':
				line = " ".join([line.strip(), "Отрезать чек\n"])
			
			
			if command == '77':
				line = " ".join([line.strip(), "Общее гашение\n"])
			
			
			if command == '79':
				line = " ".join([line.strip(), "Начало считывания штрихкода\n"])
			
			
			if command == '7A':
				line = " ".join([line.strip(), "Получить очередной блок данных\n"])
			
			
			if command == '7B':
				line = " ".join([line.strip(), "Очистить массив штрихкодов\n"])
			
			
			if command == '7C':
				line = " ".join([line.strip(), "Печать штрихкода по номеру\n"])
			
			
			if command == '7D':
				line = " ".join([line.strip(), "Состояние массива штрихкодов и картинок\n"])
			
			
			if command == '80':
				line = " ".join([line.strip(), "Открыть денежный ящик\n"])
			
			
			if command == '82':
				line = " ".join([line.strip(), "Демонстрационная печать\n"])
			
			
			if command == '84':
				line = " ".join([line.strip(), "Получение очередного блока данных ПО ККТ\n"])
			
			
			if command == '85':
				line = " ".join([line.strip(), "Импульсное открытие денежного ящика\n"])
			
			
			if command == '86':
				line = " ".join([line.strip(), "Получить очередную строку картинки по номеру\n"])
			
			
			if command == '87':
				line = " ".join([line.strip(), "Печать поля\n"])
			
			
			if command == '88':
				line = " ".join([line.strip(), "Звуковой сигнал\n"])
			
			
			if command == '8A':
				line = " ".join([line.strip(), "Очистить массив картинок\n"])
			
			
			if command == '8B':
				line = " ".join([line.strip(), "Добавить строку картинки\n"])
			
			
			if command == '8C':
				line = " ".join([line.strip(), "Статус массива картинок\n"])
			
			
			if command == '8D':
				line = " ".join([line.strip(), "Печать картинки по номеру\n"])
			
			
			if command == '8E':
				line = " ".join([line.strip(), "Печать картинки с ПК\n"])
			
			
			if command == '8F':
				line = " ".join([line.strip(), "Передать данные в порт\n"])
			
			
			if command == '90':
				line = " ".join([line.strip(), "Параметры картинки в массиве\n"])
			
			
			if command == '91':
				line = " ".join([line.strip(), "Считать регистр\n"])
			
			
			if command == '92':
				line = " ".join([line.strip(), "Открыть чек\n"])
			
			
			if command == '95':
				line = " ".join([line.strip(), "Повторная печать последнего документа\n"])
			
			
			if command == '97':
				line = " ".join([line.strip(), "Очистка буфера последнего документа\n"])
			
			
			if command == '99':
				line = " ".join([line.strip(), "Расчет по чеку\n"])
			
			
			if command == '9A':
				line = " ".join([line.strip(), "Открыть смену\n"])
			
			
			if command == '9B':
				line = " ".join([line.strip(), "Сторно расчета по чеку\n"])
			
			
			if command == '9C':
				line = " ".join([line.strip(), "Начало считывания дампа\n"])
			
			
			if command == '9D':
				line = " ".join([line.strip(), "Получение версии\n"])
			
			
			if command == '9E':
				line = " ".join([line.strip(), "Закрыть картинку\n"])
			
			
			if command == '9F':
				line = " ".join([line.strip(), "Начать считывание картинки\n"])
			
			
			if command == 'A5':
				line = " ".join([line.strip(), "Получить тип устройства\n"])
			
			
			if command == 'A6':
				line = " ".join([line.strip(), "Активизация ФН\n"])
			
			
			if command == 'A7':
				line = " ".join([line.strip(), "Закрытие архива ФН\n"])
			
			
			if command == 'A8':
				line = " ".join([line.strip(), "Печать итогов регистрации/перерегистрации ККТ\n"])
			
			
			if command == 'AB':
				line = " ".join([line.strip(), "Печать документа по номеру\n"])
			
			
			if command == 'B3':
				line = " ".join([line.strip(), "Получить последний код ошибки\n"])
			
			
			if command == 'B8':
				line = " ".join([line.strip(), "Регистрация налога на весь чек\n"])
			
			
			if command == 'C1':
				line = " ".join([line.strip(), "Печать штрихкода\n"])
			
			
			if command == 'C2':
				line = " ".join([line.strip(), "Печать штрихкода (добавление данных)\n"])
			
			
			if command == 'C3':
				line = " ".join([line.strip(), "Получить копию последнего документа (в электронном виде)\n"])
			
			
			if command == 'CE':
				
				if line[19:21] == "41":
					line = " ".join([line.strip(), "Перезагрузка ККТ\n"])
					
				else:	
					line = " ".join([line.strip(), "Выключение\n"])
			
			
			if command == 'E0':
				line = " ".join([line.strip(), "Подать питание на порт\n"])
			
			
			if command == 'E1':
				line = " ".join([line.strip(), "Отправить данные в порт\n"])
			
			
			if command == 'E2':
				line = " ".join([line.strip(), "Синхронно получить данные с порта\n"])
			
			
			if command == 'E3':
				line = " ".join([line.strip(), "Асинхронно получить данные с порта\n"])
			
			
			if command == 'E4':
				line = " ".join([line.strip(), "Настройка соединения с портом\n"])
			
			
			if command == 'E5':
				line = " ".join([line.strip(), "Запрос параметров порта\n"])
			
			
			if command == 'E6':
				line = " ".join([line.strip(), "Регистрация позиции\n"])
			
			
			if command == 'E8':
				line = " ".join([line.strip(), "Запись реквизита\n"])
			
			
			if command == 'E9':
				line = " ".join([line.strip(), "Чтение реквизита\n"])
			
			
			if command == 'EA':
				line = " ".join([line.strip(), "Комплексная команда регистрации позиции: начать формирование позиции\n"])
			
			
			if command == 'EB':
				line = " ".join([line.strip(), "Комплексная команда формирования позиции: завершить формирование позиции\n"])
			
			
			if command == 'EC':
				line = " ".join([line.strip(), "Запрос онлайн-обновления\n"])
			
			
			if command == 'ED':
				line = " ".join([line.strip(), "Программирование даты и времени\n"])
			
			
			if command == 'EE':
				line = " ".join([line.strip(), "Допечать отчета\n"])
			
			
			if command == '00':
				line = " ".join([line.strip(), "ХХ\n"])
					
			# Вариант обработки через SQL.
			#if command == '56':
			#	hex_2 = line[19:21],
			#	cursor.execute("SELECT DESC FROM REGIME WHERE HEX = ?", hex_2)				
			#	line = " ".join([line.rstrip(), "Вход в режим", cursor.fetchone()[0], "\n"])
			#
			#		
			#elif command == 'CE':
			#	if line [19:21] == "41":  # Не меняй способ обработки CE, здесь нужно именно так!
			#		line = " ".join([line.rstrip(), "Перезагрузка ККТ\n"])
			#	else:
			#		line = " ".join([line.rstrip(), "Выключение\n"])
			#
			#
			#elif command == 'A4':
			#	hex_2 = line[19:21],
			#	cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'A4' AND HEX_2 = ?", hex_2)				
			#	line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
			#
			#
			#elif command == 'EF':
			#	hex_2 = line[19:21],
			#	cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = 'EF' AND HEX_2 = ?", hex_2)				
			#	line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])
			#
			#
			#else:
			#	cursor.execute("SELECT DESC FROM COMMAND WHERE HEX = ?", (command,))
			#	line = " ".join([line.rstrip(), cursor.fetchone()[0], "\n"])v
			#

			
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