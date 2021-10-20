import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "sys"))
from dict import dict, check
import ops


# Тестовый режим
InTest = 1
TestInputFile = 'logs.txt'


# Определение рабочей папки для i-того количества входящих файлов
if len(sys.argv) > 1: 
	os.chdir(os.path.dirname(sys.argv[1]))
elif InTest == 0:
	print("Скрипт работает только если перетянуть на него файлы логов ККТ.\n")
	os.system("pause")
	quit()

print("Сформированы файлы:")
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

			#
			# ОПЕРАЦИИ ОБРАБОКИ СТРОК:
			#
			
			# 1. Перезаписывает некоторые строки на идентичные:
			ops.nothing(line, output)

			# 2.
			
			# 3.
			
			# 4.
			
			# 5.
			
			#
			# КОНЕЦ ОБРАБОТОК СТРОК
			#

	print("", outputf)
print("Работа завершена.\n")
#os.system("pause")
