' Хули тебе надо-то тут, блядь?
'
' Шучу. Этот скрипт запускает evo_kkm_reader.py с первым аргументом. Это нужно
' только для работы контекстного меню Windows. Лучше всего запускать так:
' "wscript" "%%path%%\sys\contextRun.vbs" //Nologo "%1"
'
' Вне применения для контекстного меню этот скрипт НЕ НУЖЕН.

dieBitch = Replace(WScript.ScriptFullName&"*",WScript.ScriptName&"*","") ' pathTo
hateIt = CHR(34) & WScript.Arguments(0) & CHR(34) ' путь файла в кавычки для поддержки путей с пробелами
WScript.CreateObject("Shell.Application").ShellExecute Left(dieBitch,len(dieBitch)-4)&"kkm_reader.py",hateIt,,,0
