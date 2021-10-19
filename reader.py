import os, sys
from dict import dict
p
# Рабочая папка
os.chdir(os.path.dirname(sys.argv[0]))

# Проверка на drag & drop
if len(sys.argv) == 2:
	inputf = os.path.basename(sys.argv[1])
	outputf = "output_" + os.path.basename(sys.argv[1])
else: # Имена файлов по-умолчанию если нет drag & drop
	inputf = 'logs.txt'
	outputf = 'outoput_logs.txt'



flush = open(outputf, 'w')
flush.close()



def convert(text):	# Обработка текста в строке
	output = open(outputf, 'a', encoding='cp1251')
	header = text[0:20]
	if header[15] == '>': # Четырежды >
		text = text[0:13] + '>>>>> ' + text[21:]
		output.writelines(text)
	else:
	
	
	
		output.writelines(text)
		output.close()

file = open(inputf) # Передача строки на обработку
try:
	for row in file:
		convert(row)
finally:
	file.close()



#print(sys.argv[0])
os.system("pause")