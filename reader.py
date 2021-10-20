import os, sys, dict
from dict import dict

dict.check()

# Тестовый режим
InTest = 1
TestInputFile = 'logs.txt'

# Рабочая папка
#os.chdir(os.path.dirname(sys.argv[0]))

# Определение рабочей папки
if len(sys.argv) > 1: 
	os.chdir(os.path.dirname(sys.argv[1]))
elif InTest == 0:
	print("Для обработки логов перетяните их на файл скрипта.\nРабота завершена.\n")
	quit()


for i in range(len(sys.argv)):
	if len(sys.argv) > 1: # Проверка на drag & drop
		inputf = os.path.basename(sys.argv[i+1])
		outputf = "output_" + os.path.basename(sys.argv[i+1])
	elif InTest == 1: # Имена файлов по-умолчанию для тестового режима
		os.chdir(os.path.dirname(sys.argv[0]))
		inputf = TestInputFile
		outputf = 'output_logs.txt'	
	with open(inputf, 'r', encoding='utf-8') as input, open(outputf, 'w', encoding='utf-8') as output:
		for line in input:
			if len(line) > 10:  # проверка для обработки пустых строк
				if line[15] == '>':
					line = line[0:13] + '>>>> ' + line[18:]
			output.write(line)
	
print("Готово\n")
os.system("pause")