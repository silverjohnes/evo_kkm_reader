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
import zipfile
sys.path.append(os.path.join(os.path.dirname(__file__), 'sys'))
import process


inTest = 0
autoOpen = 1
autoOpenZip = 1
testInputFile = 'logs.txt'
outputPrefix = 'readable_'
supportedFileTypes = ('.txt', '.zip')



#  Разбор типов файлов.
def checkFile(): 
	global isZip
	fname, fext = os.path.splitext(inputFile)
	if fext.lower() in supportedFileTypes:
		if zipfile.is_zipfile(inputFile):
			isZip = 1
			zipRoutine(fname)
		else:
			isZip = 0
			fileProcess()

#  Тут всё понятно.
def zipRoutine(fname):
	global inputFile
	beforeZipDir = os.getcwd()
	#  Очистка целевой папки для разархивирования, если она есть.
	for unzipFolder, insideDirs, insideFiles in os.walk(os.path.join(os.getcwd(), fname), topdown=False):
		for file in insideFiles:
			os.remove(os.path.join(unzipFolder, file))
		for file in insideDirs:
			os.rmdir(os.path.join(unzipFolder, file))
	#
	with zipfile.ZipFile(inputFile, 'r') as inputZipFile:
		for zipFileList in inputZipFile.infolist(): #  Исключение папок из распаковки.
			if zipFileList.filename[-1] == '/':
				continue
			zipFileList.filename = os.path.basename(zipFileList.filename)
			inputZipFile.extract(zipFileList, os.path.join(os.getcwd(), fname))
	os.chdir(os.path.join(os.getcwd(), fname))
	for j in range(len(os.listdir())):
		inputFile = os.listdir()[j]
		fileProcess()
	for files in os.listdir(): #  Очистка папки от необработанных оригиналов.
		if os.path.basename(files)[0:len(outputPrefix)] != outputPrefix:
			os.remove(os.path.basename(files))
	if autoOpenZip == 1:
		os.system(f'start {os.path.realpath(os.getcwd())}')
	os.chdir(beforeZipDir)
	

#  Обработчик файлов.
def fileProcess():
	outputFile = outputPrefix + inputFile
	command = "00" #  Управляющая команда, на которую обрабатывается ответ.  
	with open(inputFile, 'r', encoding='utf-8') as input, open(outputFile, 'w', encoding='utf-8') as output:
		for line in input:
			if line[14:16] == "> ":
				command = line[16:18]
			output.write(process.process(line, command)) #  То, ради чего всё затевалось.
	if inTest == 0 and isZip == 0:
		os.remove(inputFile)
	elif autoOpen == 1 and isZip == 0:
		os.system(f'start {outputFile}')
	print(">", outputFile)


#  Основное тело.
if len(sys.argv) > 1: 
	os.chdir(os.path.dirname(sys.argv[1]))
	for i in range(1, len(sys.argv)):
		inputFile = os.path.basename(sys.argv[i])
		checkFile()
elif inTest == 1:
	os.chdir(os.path.dirname(__file__))
	inputFile = testInputFile
	checkFile()
else:
	print("Перетяните файлы с логами из любой папки на", os.path.basename(__file__), "\n")
	if sys.platform == 'win32':
		os.system('pause')
	else:
		input("Для продолжения нажмите Enter . . .")
	quit()

print()