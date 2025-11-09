# 1. Вывести доступное дисковое пространство для всех дисков, но в формате - только название диска и доступное пространство.
# 2. Из файла /etc/group подсчитать количество строк, где строка содержит слово root с использованием grep wc из файла с разделителем.
# 3. Из того же файла - вывести только 2 столбец. Сколько x и сколько * ?
# 4. Проверить, что можно работать с разделителем.
# 5. Записать последние 3 строки из файла /etc/group в отдельный файл и в нем при помощи sed заменить 1000 на 777.
# 6. При помощи текстового редактора заменить в файле /tmp/file user2 на user1 user2 user3 соответственно.
# 7. Дописать в файл /tmp/file всех пользователей из /etc/passwd (первый столбец)
# 8. При помощи sed дописать в начале каждой строки слово Username.

   0 df -h
   1 df -h | awk {'print $1, $4'}
   2 cat /etc/group
   3 cat /etc/group | grep "user2" | wc -l
   4 cat /etc/group | grep "root" | wc -l
   5 cat /etc/group | awk -F: '{print $2}' | grep x | wc -l
   6 cat /etc/group | awk -F: '{print $2}' | grep -v x | wc -l
   7 cat /etc/group | awk -F: '{print $2}' | grep * | wc -l
   8 sed -i 's/1000/777/
   9 touch /tmp/file
  10 sed -i 's/1000/777/g' /tmp/file
  11 cat /tmp/file
  12 cat /etc/group | tail -3 /tmp/file
  13 cat /tmp/file
  14 cat /etc/group | tail -3 >> /tmp/file
  15 cat /tmp/file
  16 sed -i 's/1000/777/g' /tmp/file
  17 cat /tmp/file
  18 vi /tmp/file
  19 cat /tmp/file
  20 vi /tmp/file
  21 cat /tmp/file
  22 cat /etc/passwd | awk -F: '{print $1}' >> /tmp/file
  23 cat /tmp/file
  24 sed -i 's/^/Username: /' /tmp/file
  25 cat /tmp/file
  26 history > /tmp/classwork07.sh && export_file /tmp/classwork07.sh
