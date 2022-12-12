# mzgb-reg
# Обновить chrome до последней версии
# Скачать и установить python выбрать 
https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

# установить зависимости
pip install PyInstaller
pip install selenium==4.2.0

# Скачать и распокавать в папку 
https://github.com/pwddel/mzgb-reg/archive/refs/heads/main.zip

# Сборка
pyinstaller --onefile main.py

# Запуск
main.exe
