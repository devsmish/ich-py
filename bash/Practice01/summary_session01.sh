# 1. Создайть папку ВАШЕ_ИМЯ по полному пути: /opt/test/ВАШЕ_ИМЯ
# 2. Зайти в новую папку
# 3. Создать файл с именем file.txt
# 4. Выйти в домашнюю директорию
# 5. Скопировать файл file.txt в папку /tmp с переименованием file2.txt
# 6. Удалить файл file.txt
# 7. Проверить наличия нового файла file.txt
mkdir -p /opt/test/ivan
cd /opt/test
touch file.txt
cd
cp /opt/test/file.txt /tmp/file.txt
rm -rf /opt/test/file.txt
ls /tmp