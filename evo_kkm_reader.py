#!/usr/bin/env python3
# =============================================================
# Скрипт для упрощения восприятия логов ККТ, используемых в ККТ 
# Эвотор и АТОЛ, версия протокола 3.1.
# В случае разночтений — приоритет Эвотору.
#
# Автор  : Silver Johnes (silver.johnes@gmail.com)
# =============================================================
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'sys'))
import ops


inTest = 1
testInputFile = 'logs.txt'
outputPrefix = 'output_'


# Определение рабочей папки для i-того количества входящих файлов
if len(sys.argv) > 1: 
	os.chdir(os.path.dirname(sys.argv[1]))
elif inTest == 0:
	print("Скрипт работает только если перетянуть на него файлы логов ККТ.\n")
	os.system("pause")
	quit()

print("Сформированы файлы:")
for i in range(len(sys.argv)):
	if len(sys.argv) > 1: # Проверка на drag & drop
		inputFile = os.path.basename(sys.argv[i+1])
	elif inTest == 1: # Переменные для тестового режима
		os.chdir(os.path.dirname(__file__))
		inputFile = testInputFile
	outputFile = outputPrefix + inputFile
	with open(inputFile, 'r', encoding='utf-8') as input, open(outputFile, 'w', encoding='utf-8') as output:
		for line in input:
			output.write(ops.linewrapper(line)) # То, ради чего всё затевалось
			

	print("", outputFile) # Перечисление обработанных файлов
print("Работа завершена.\n")
#os.system("pause")