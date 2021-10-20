import os, sys
from dict import dict

# Тестовый режим
InTest = 1

# Рабочая папка
#os.chdir(os.path.dirname(sys.argv[0]))

# Проверка на drag & drop
if len(sys.argv) > 1:
	os.chdir(os.path.dirname(sys.argv[1]))
	inputf = os.path.basename(sys.argv[1])
	outputf = "output_" + os.path.basename(sys.argv[1])
elif InTest == 1:	# Имена файлов по-умолчанию для тестового режима
	os.chdir(os.path.dirname(sys.argv[0]))
	inputf = 'logs-long.txt'
	outputf = 'output_logs.txt'
else:
	print("Для обработки логов перетяните их на файл скрипта.\nРабота завершена.\n")
	quit()

with open(inputf, 'r', encoding='utf-8') as input, open(outputf, 'w', encoding='utf-8') as output:
	for line in input:
		if len(line) > 10:  # проверка для обработки пустых строк
			if line[15] == '>':
				line = line[0:13] + '>>>> ' + line[18:]
		output.write(line)

#os.system("pause")