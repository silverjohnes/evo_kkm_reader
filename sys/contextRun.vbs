' Хули тебе надо-то тут, блядь?
'
' Шучу. Этот скрипт запускает evo_kkm_reader.py с первым аргументом. Это нужно
' только для работы контекстного меню Windows. Лучше всего запускать так:
' "wscript" "%%path%%\sys\contextRun.vbs" //Nologo "%1"
'
' Вне применения для контекстного меню этот скрипт НЕ НУЖЕН.

dieBitch = Replace(WScript.ScriptFullName&"*",WScript.ScriptName&"*","") 'pathTo
WScript.CreateObject("Shell.Application").ShellExecute Left(dieBitch,len(dieBitch)-4)&"evo_kkm_reader.py",WScript.Arguments(0) 'removing /sys from the path