# Расшифровка логов ККТ.
Базовая расшифровка логов ККТ формата АТОЛ 3.1 в исполнении Эвотора.

## Установка 
1. Проверьте наличие или установите Python версии 3.х (https://www.python.org/downloads/).
2. Скачайте архив с программой, разархивируйте в постоянную папку.
3. Windows: запустите файл интеграции в контекстное меню с правами Администратора.
4. Windows: Перезагрузите компьютер и можно пользоваться.
5. Windows: Желательно использовать многооконный текстовый редактор типа Notepad++ вместо стандартного Блокнота.
6. Остальные ОС: Можно пользоваться сразу, но интеграции в контекстное меню нет.

## Использование:
1. Windows: через контекстное меню «Обработать логи ККТ» на zip-архиве или одиночном файле с логом ККТ. В первый раз нужно дать разрешение на запуск, потом спрашивать не будет.
2. Все остальные ОС: запустить kkm_reader.py с аргументами в виде списка файлов (можно drag & drop).
3. Рекомендую установить много-оконный текстовый редактор в качестве редактора по-умолчанию, так как в случае обработки нескольких файлов открываться будут они все. Для Windows это может быть Notepad++.

Программа работает с логами в форматах .txt и .zip (с папками не работает). После обработки текстовых файлов они открываются в текстовом редакторе, после обработки архивов открываются папки с обработанными файлами. Эту автоматизацию можно отключить внутри исполняемого файла.
