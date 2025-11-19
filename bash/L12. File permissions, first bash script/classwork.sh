# добавление прав на чтение и запись для владельца и только чтение для групп и остальніх на файл
chmod 644 file.txt
# Добавить право чтения для владельца файла
chmod u+r file.txt
# Убрать право записи для группы и остальных пользователей
chmod go-w file.txt
# добавление для всех права на выполнение файла
chmod a+x script.sh
# Добавить право выполнения для всех пользователей к файлу script.sh
chmod +x script.sh
# Установить владельцу права на чтение и запись, а для группы и остальных пользователей только на чтение к файлу file.txt
chmod u=rw,go=r file.txt
# Рекурсивно установить права на чтение, запись и выполнение для владельца, и на чтение и выполнение для группы и
# остальных пользователей для всех файлов и директорий внутри directory.
chmod -R 755 directory
# Задание
# 1. Создать новый файл script.sh и записать в него:
  ##!/bin/bash
  #echo Hello
  #date
cd /opt/101025-ptm/SMyshynskyi/
touch script.sh
# 2. Выйти из нового файла, сохранив его. CTRL+O and CTRL+X
nano script.sh
# 3. Сделать текстовый файл исполняемым, используя chmod +x или chmod u+x script.sh
chmod u+x script.sh
# 4. Запуск скрипта
./script.sh
/opt/101025-ptm/SMyshynskyi/script.sh
bash script.sh
# 5. Добавить в скрипт комментарий и переменную так, чтобы при исполнении получить Hello Ваше имя
nano script.sh
#!/bin/bash
# NAME=Serhii

# echo Hello $NAME

# current date
# date