' Хули тебе надо-то тут, блядь?
'
' Шучу. Этот скрипт запускает evo_kkm_reader.py с первым аргументом. Это нужно
' только для работы контекстного меню Windows. Лучше всего запускать так:
' "wscript" "%%path%%\contextRun.vbs" //Nologo "%1"
'
' Вне применения для контекстного меню этот скрипт НЕ НУЖЕН.

WScript.CreateObject("Shell.Application").ShellExecute Replace(WScript.ScriptFullName&"*",WScript.ScriptName&"*","")&"evo_kkm_reader.py",WScript.Arguments(0)