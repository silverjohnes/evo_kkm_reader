#!/usr/bin/env python3
# ==============================================================
# Скрипт для расшифровки логов ККТ в формате АТОЛ для упрощения
#  чтения логов человеком. Разночтения между АТОЛом и Эвотором
#  трактуются в пользу варианта, который реализован в Эвоторе.
#
#       http://github.com/silverjohnes/evo_kkm_reader
# ==============================================================
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'sys'))
import process


inTest = 0
testInputFile = 'logs.txt'
outputPrefix = 'processed_'


# Обработчик файлов.
def fileProcess():
	outputFile = outputPrefix + inputFile
	command = "00" # Управляющая команда, на которую обрабатывается ответ.  
	with open(inputFile, 'r', encoding='utf-8') as input, open(outputFile, 'w', encoding='utf-8') as output:
		for line in input:
			if line[14:16] == "> ":
				command = line[16:18]
			output.write(process.process(line, command)) # То, ради чего всё затевалось.
	print(">", outputFile)


# Определение рабочей папки или отбивка.
if len(sys.argv) > 1: 
	os.chdir(os.path.dirname(sys.argv[1]))
elif inTest == 0:
	print("Перетяните файлы с логами из любой папки на", os.path.basename(__file__), "\n")
	if sys.platform == 'win32':
		os.system('pause')
	else:
		input("Для продолжения нажмите Enter . . .")
	quit()


# Беги, глупец
print("Сформированы файлы:")
if len(sys.argv) > 1: # Есть параметры запуска?
	for i in range(1, len(sys.argv)):
		inputFile = os.path.basename(sys.argv[i])
		fileProcess()
elif inTest == 1: # Фигачу тестовый файл если включен тестовый режим
	os.chdir(os.path.dirname(__file__))
	inputFile = testInputFile
	fileProcess()
	
	
print()
