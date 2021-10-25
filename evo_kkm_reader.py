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


inTest = 1
testInputFile = 'logs.txt'
outputPrefix = 'processed_'


# Определение рабочей папки для i-того количества входящих файлов.  
if len(sys.argv) > 1: 
	os.chdir(os.path.dirname(sys.argv[1]))
elif inTest == 0:
	print("Перетяните файлы с логами из любой папки на", os.path.basename(__file__), "\n")
	os.system("pause")
	quit()


print("Сформированы файлы:")
for i in range(len(sys.argv)):
	if len(sys.argv) > 1: # Проверка на drag & drop.  
		inputFile = os.path.basename(sys.argv[i+1])
	elif inTest == 1: # Переменные для тестового режима:  
		os.chdir(os.path.dirname(__file__))
		inputFile = testInputFile
	outputFile = outputPrefix + inputFile
	command = "00" # Управляющая команда, на которую обрабатывается ответ.  
	with open(inputFile, 'r', encoding='utf-8') as input, open(outputFile, 'w', encoding='utf-8') as output:
		for line in input:
			if line[14:16] == "> ":
				command = line[16:18]
			output.write(process.process(line, command)) # То, ради чего всё затевалось.
			

	print("", outputFile)
print("Работа завершена.\n")
#os.system("pause")