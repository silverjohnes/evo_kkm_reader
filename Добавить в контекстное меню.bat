::
:: Включение программы в контекстное меню проводника.
::

 @echo off
 CHCP 1251
 CLS

:: Evaluate, see "https://stackoverflow.com/a/12264592/1016343" for description.
:init
 setlocal DisableDelayedExpansion
 set cmdInvoke=1
 set winSysFolder=System32
 set "batchPath=%~0"
 for %%k in (%0) do set batchName=%%~nk
 set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
 setlocal EnableDelayedExpansion
:checkPrivileges
  NET FILE 1>NUL 2>NUL
  if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )
:getPrivileges
  if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
  ECHO Запрос прав администратора.
  ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
  ECHO args = "ELEV " >> "%vbsGetPrivileges%"
  ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
  ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
  ECHO Next >> "%vbsGetPrivileges%"
  if '%cmdInvoke%'=='1' goto InvokeCmd 
  ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
  goto ExecElevation
:InvokeCmd
  ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
  ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"
:ExecElevation
 "%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
 exit /B
:gotPrivileges
 setlocal & cd /d %~dp0
 if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)
 :: End of evaluation.


 REG ADD "HKEY_CLASSES_ROOT\*\shell\evo_kkm_reader" /v MUIVerb /t REG_SZ /d "Обработать логи ККТ" /f
::REG ADD "HKEY_CLASSES_ROOT\*\shell\evo_kkm_reader" /v Position /t REG_SZ /d "Top" /f
 REG ADD "HKEY_CLASSES_ROOT\*\shell\evo_kkm_reader" /v Icon /t REG_EXPAND_SZ /d "%~dp0sys\icon.ico" /f
 REG ADD "HKEY_CLASSES_ROOT\*\shell\evo_kkm_reader\command" /ve /d "\"wscript\" \"%~dp0sys\context_run.vbs\" //Nologo \"%%1\"" /f

 ECHO.
 ECHO Настройки будут применены после перезагрузки компьютера.
 ECHO.
 PAUSE
