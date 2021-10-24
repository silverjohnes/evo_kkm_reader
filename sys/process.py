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
				var = line[19:21],
				cursor.execute("SELECT DESC FROM REGIME WHERE HEX = ?", var)				
				line = " ".join([line.rstrip(), "Вход в режим", cursor.fetchone()[0], "\n"])
			
			'''			
			if command == '56':
				line = line.rstrip() + " Вход в режим"
				var = line[19:21],
				cursor.execute("SELECT DESC FROM REGIME WHERE HEX = ?", var)
				line = line.rstrip() + cursor.fetchone()[0] + "\n"'''
				
				
			if command == '3F':
				line = line.rstrip() + " Запрос состояния ККТ\n"
			
			
			if command == '43':
				line = line.rstrip() + " Скидка\n"
			
			
			if command == '45':
				line = line.rstrip() + " Запрос кода состояния ККТ\n"
			
			
			if command == '46':
				line = line.rstrip() + " Чтение таблицы\n"
			
			
			if command == '47':
				line = line.rstrip() + " Гудок\n"
			
			
			if command == '48':
				line = line.rstrip() + " Выход из текущего режима\n"
			
			
			if command == '49':
				line = line.rstrip() + " Внесение денег\n"
			
			
			if command == '4A':
				line = line.rstrip() + " Закрыть чек (со сдачей)\n"
			
			
			if command == '4B':
				line = line.rstrip() + " Программирование времени\n"
			
			
			if command == '4C':
				line = line.rstrip() + " Печать строки\n"
			
			
			if command == '4D':
				line = line.rstrip() + " Запрос наличных\n"
			
			
			if command == '4F':
				line = line.rstrip() + " Выплата денег\n"
			
			
			if command == '50':
				line = line.rstrip() + " Программирование таблицы\n"
			
			
			if command == '58':
				line = line.rstrip() + " Получение последнего сменного итога\n"
			
			
			if command == '59':
				line = line.rstrip() + " Аннулирование всего чека\n"
			
			
			if command == '5A':
				line = line.rstrip() + " Снятие суточного отчета с гашением (закрытие смены)\n"
			
			
			if command == '61':
				line = line.rstrip() + " Ввод заводского номера\n"
			
			
			if command == '62':
				line = line.rstrip() + " Активизация памяти ПД\n"
			
			
			if command == '64':
				line = line.rstrip() + " Программирование даты\n"
			
			
			if command == '65':
				line = line.rstrip() + " Отчет ППД по диапазону дат\n"
			
			
			if command == '66':
				line = line.rstrip() + " Отчет ППД по диапазону смен\n"
			
			
			if command == '67':
				line = line.rstrip() + " Начало снятия отчета без гашения\n"
			
			
			if command == '6B':
				line = line.rstrip() + " Технологическое обнуление ККТ\n"
			
			
			if command == '6C':
				line = line.rstrip() + " Печать клише чека\n"
			
			
			if command == '6D':
				line = line.rstrip() + " Ввод кода защиты ККТ\n"
			
			
			if command == '71':
				line = line.rstrip() + " Инициализация таблиц нач. значениями\n"
			
			
			if command == '73':
				line = line.rstrip() + " Печать нижней части чека\n"
			
			
			if command == '74':
				line = line.rstrip() + " Запрос активизированности кода защиты ККТ\n"
			
			
			if command == '75':
				line = line.rstrip() + " Отрезать чек\n"
			
			
			if command == '77':
				line = line.rstrip() + " Общее гашение\n"
			
			
			if command == '79':
				line = line.rstrip() + " Начало считывания штрихкода\n"
			
			
			if command == '7A':
				line = line.rstrip() + " Получить очередной блок данных\n"
			
			
			if command == '7B':
				line = line.rstrip() + " Очистить массив штрихкодов\n"
			
			
			if command == '7C':
				line = line.rstrip() + " Печать штрихкода по номеру\n"
			
			
			if command == '7D':
				line = line.rstrip() + " Состояние массива штрихкодов и картинок\n"
			
			
			if command == '80':
				line = line.rstrip() + " Открыть денежный ящик\n"
			
			
			if command == '82':
				line = line.rstrip() + " Демонстрационная печать\n"
			
			
			if command == '84':
				line = line.rstrip() + " Получение очередного блока данных ПО ККТ\n"
			
			
			if command == '85':
				line = line.rstrip() + " Импульсное открытие денежного ящика\n"
			
			
			if command == '86':
				line = line.rstrip() + " Получить очередную строку картинки по номеру\n"
			
			
			if command == '87':
				line = line.rstrip() + " Печать поля\n"
			
			
			if command == '88':
				line = line.rstrip() + " Звуковой сигнал\n"
			
			
			if command == '8A':
				line = line.rstrip() + " Очистить массив картинок\n"
			
			
			if command == '8B':
				line = line.rstrip() + " Добавить строку картинки\n"
			
			
			if command == '8C':
				line = line.rstrip() + " Статус массива картинок\n"
			
			
			if command == '8D':
				line = line.rstrip() + " Печать картинки по номеру\n"
			
			
			if command == '8E':
				line = line.rstrip() + " Печать картинки с ПК\n"
			
			
			if command == '8F':
				line = line.rstrip() + " Передать данные в порт\n"
			
			
			if command == '90':
				line = line.rstrip() + " Параметры картинки в массиве\n"
			
			
			if command == '91':
				line = line.rstrip() + " Считать регистр\n"
			
			
			if command == '92':
				line = line.rstrip() + " Открыть чек\n"
			
			
			if command == '95':
				line = line.rstrip() + " Повторная печать последнего документа\n"
			
			
			if command == '97':
				line = line.rstrip() + " Очистка буфера последнего документа\n"
			
			
			if command == '99':
				line = line.rstrip() + " Расчет по чеку\n"
			
			
			if command == '9A':
				line = line.rstrip() + " Открыть смену\n"
			
			
			if command == '9B':
				line = line.rstrip() + " Сторно расчета по чеку\n"
			
			
			if command == '9C':
				line = line.rstrip() + " Начало считывания дампа\n"
			
			
			if command == '9D':
				line = line.rstrip() + " Получение версии\n"
			
			
			if command == '9E':
				line = line.rstrip() + " Закрыть картинку\n"
			
			
			if command == '9F':
				line = line.rstrip() + " Начать считывание картинки\n"
			
			
			if command == 'A4':
				fncommand = line[19:21]
				
				if fncommand == "10":
					line = line.rstrip() + " Запрос параметров текущей смены\n"
					
				if fncommand == "20":
					line = line.rstrip() + " Получить статус информационного обмена с ФН\n"
					
				if fncommand == "30":
					line = line.rstrip() + " Запрос статуса ФН\n"
					
				if fncommand == "31":
					line = line.rstrip() + " Запрос номера ФН\n"
					
				if fncommand == "32":
					line = line.rstrip() + " Запрос срока действия ФН\n"
					
				if fncommand == "33":
					line = line.rstrip() + " Запрос версии ФН\n"
					
				if fncommand == "35":
					line = line.rstrip() + " Запрос последних ошибок ФН\n"
					
				if fncommand == "40":
					line = line.rstrip() + " Найти фискальный документ по номеру\n"
					
				if fncommand == "41":
					line = line.rstrip() + " Запрос квитанции о получении фискального документа ОФД по номеру документа\n"
					
				if fncommand == "42":
					line = line.rstrip() + " Запрос количества ФД, на которые нет квитанции\n"
					
				if fncommand == "43":
					line = line.rstrip() + " Запрос итогов фискализации ФН\n"
					
				if fncommand == "44":
					line = line.rstrip() + " Запрос параметра фискализации ФН\n"
					
				if fncommand == "45":
					line = line.rstrip() + " Запрос фискального документа в TLV формате\n"
					
				if fncommand == "46":
					line = line.rstrip() + " Чтение TLV фискального документа\n"
					
				if fncommand == "47":
					line = line.rstrip() + " Чтение TLV параметров фискализации\n"
					
				if fncommand == "60":
					line = line.rstrip() + " Инициализация массо-габаритного макета ФН\n"
			
			
			if command == 'A5':
				line = line.rstrip() + " Получить тип устройства\n"
			
			
			if command == 'A6':
				line = line.rstrip() + " Активизация ФН\n"
			
			
			if command == 'A7':
				line = line.rstrip() + " Закрытие архива ФН\n"
			
			
			if command == 'A8':
				line = line.rstrip() + " Печать итогов регистрации/перерегистрации ККТ\n"
			
			
			if command == 'AB':
				line = line.rstrip() + " Печать документа по номеру\n"
			
			
			if command == 'B3':
				line = line.rstrip() + " Получить последний код ошибки\n"
			
			
			if command == 'B8':
				line = line.rstrip() + " Регистрация налога на весь чек\n"
			
			
			if command == 'C1':
				line = line.rstrip() + " Печать штрихкода\n"
			
			
			if command == 'C2':
				line = line.rstrip() + " Печать штрихкода (добавление данных)\n"
			
			
			if command == 'C3':
				line = line.rstrip() + " Получить копию последнего документа (в электронном виде)\n"
			
			
			if command == 'CE':
				
				if line[19:21] == "41":
					line = line.rstrip() + " Перезагрузка ККТ\n"
					
				else:	
					line = line.rstrip() + " Выключение\n"
			
			
			if command == 'E0':
				line = line.rstrip() + " Подать питание на порт\n"
			
			
			if command == 'E1':
				line = line.rstrip() + " Отправить данные в порт\n"
			
			
			if command == 'E2':
				line = line.rstrip() + " Синхронно получить данные с порта\n"
			
			
			if command == 'E3':
				line = line.rstrip() + " Асинхронно получить данные с порта\n"
			
			
			if command == 'E4':
				line = line.rstrip() + " Настройка соединения с портом\n"
			
			
			if command == 'E5':
				line = line.rstrip() + " Запрос параметров порта\n"
			
			
			if command == 'E6':
				line = line.rstrip() + " Регистрация позиции\n"
			
			
			if command == 'E8':
				line = line.rstrip() + " Запись реквизита\n"
			
			
			if command == 'E9':
				line = line.rstrip() + " Чтение реквизита\n"
			
			
			if command == 'EA':
				line = line.rstrip() + " Комплексная команда регистрации позиции: начать формирование позиции\n"
			
			
			if command == 'EB':
				line = line.rstrip() + " Комплексная команда формирования позиции: завершить формирование позиции\n"
			
			
			if command == 'EC':
				line = line.rstrip() + " \n"
			
			
			if command == 'ED':
				line = line.rstrip() + " Программирование даты и времени\n"
			
			
			if command == 'EE':
				line = line.rstrip() + " Допечать отчета\n"
			
			
			if command == 'EF':
				subcommand = line[19:21]
				
				if subcommand == "00":
					line = line.rstrip() + " Получить статус ЭЖ\n"
					
				if subcommand == "01":
					line = line.rstrip() + " Начать чтение записии из ЭЖ\n"
					
				if subcommand == "02":
					line = line.rstrip() + " Получить следующую TLV запись из ЭЖ\n"
					
				if subcommand == "03":
					line = line.rstrip() + " Очистить ЭЖ\n"
			
			
			if command == '00':
				line = line.rstrip() + " ХХ\n"
			
			
			
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
