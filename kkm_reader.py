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
import subprocess


inTest = 0
autoOpen = 1
autoOpenZip = 1
slugClearance = 1  #  Очистка от строк обмена (>>>> и <<<<)
outputPrefix = 'readable_'
testInputFile = 'logs.txt'
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
	#  Очистка целевой папки для разархивирования, если она есть:
	for unzipFolder, insideDirs, insideFiles in \
	os.walk(os.path.join(os.getcwd(), fname), topdown=False):
		for file in insideFiles:
			os.remove(os.path.join(unzipFolder, file))
		for file in insideDirs:
			os.rmdir(os.path.join(unzipFolder, file))
	#  Распаковка содержимого архива (без папок):
	with zipfile.ZipFile(inputFile, 'r') as inputZipFile:
		for zipFileList in inputZipFile.infolist(): 
			if zipFileList.filename[-1] == '/':
				continue
			zipFileList.filename = os.path.basename(zipFileList.filename)
			inputZipFile.extract(zipFileList, os.path.join(os.getcwd(), fname))
	#  Обработка разархивированного
	os.chdir(os.path.join(os.getcwd(), fname))
	for j in range(len(os.listdir())):
		inputFile = os.listdir()[j]
		fileProcess()
	#  Очистка папки от необработанных оригиналов:
	for files in os.listdir(): 
		if os.path.basename(files)[0:len(outputPrefix)] != outputPrefix:
			os.remove(os.path.basename(files))
	#
	if autoOpenZip == 1:
		openFile(os.getcwd())
	os.chdir(beforeZipDir)
	

#  Обработчик файлов.
def fileProcess():
	outputFile = outputPrefix + inputFile
	command = "00"
	wholeCommandLine = ""
	answerLine = ""
	#pastCommand = ""
	with open(inputFile, 'r', encoding='utf-8') as input, \
	open(outputFile, 'w', encoding='utf-8') as output:
		for line in input:
			if line[15:16] == ">" or line[15:16] == "<":
				if slugClearance == 1: 
					continue
			elif line[14:16] == "> ":
				command = line[16:18]
				wholeCommandLine = line
			elif line[14:16] == "< ":
				answerLine = line
			#  То, ради чего всё затевалось:
			output.write(process.process(line, wholeCommandLine, command, \
			answerLine))

	print(">", outputFile)
	if isZip == 0:
		#if inTest == 0:
		#	os.remove(inputFile)
		if autoOpen == 1:
			openFile(outputFile)


#  ОС-независимая открывашка файлов после обработки.
def openFile(fileOrPathToOpen):
	if sys.platform == "win32":
		os.startfile(os.path.realpath(fileOrPathToOpen))
	else:
		opener = "open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call([opener, os.path.realpath(fileOrPathToOpen)])


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
	print("Для обработки логов перетяните файлы с логами из любой папки на",
	os.path.basename(__file__), "\n\nЕсли вы запускаете программу правильно, "
	"но видите это сообщение,\nубедитесь, что в качестве "
	"программы по-умолчанию для открытия\nфайлов с расширением .py "
    "стоит %WINDIR%\py.exe\n\n")
	if sys.platform == 'win32':
		os.system('pause')
	else:
		input("Для продолжения нажмите Enter . . .")
	quit()


#  Удаление устаревшего файла.
os.chdir(os.path.dirname(__file__))
try:
	os.remove('process.py')
except:
	pass
#print()
