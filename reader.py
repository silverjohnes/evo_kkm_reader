import os, sys
import win_unicode_console
from dict import dict

win_unicode_console.enable()


# Рабочая папка
os.chdir(os.path.dirname(sys.argv[0]))

# Проверка на drag & drop
if len(sys.argv) > 1:
	inputf = os.path.basename(sys.argv[1])
	outputf = "output_" + os.path.basename(sys.argv[1])
else: # Имена файлов по-умолчанию если нет drag & drop
	inputf = 'logs-long.txt'
	outputf = 'output_logs.txt'


# Очистка файла вывода если он существует
flush = open(outputf, 'w')
flush.close()



def convert(text):	# Обработка текста в строке
	output = open(outputf, 'a', encoding='utf-8')
	header = text[0:20]
	if header[15] == '>':
		text = text[0:13] + '>>>> ' + text[21:]
		output.writelines(text)
	else:
		output.writelines(text)
	output.close()


file = open(inputf, encoding='utf-8') # Передача строки на обработку
try:
	for row in file:
		convert(row)
finally:
	file.close()




os.system("pause")