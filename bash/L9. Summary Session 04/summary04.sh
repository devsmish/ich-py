ps -ef | sshd -D /*демон, который слушает входящие ssh-соединения*/
w просмотр списка подключенных пользователей
cd C:\Users\devsm\.ssh\
# Аналог cat в Windows
type id_ed25519.pub
# 1. Зайти на сервер.
# 2. Проверить наличие папки со своим именем по пути /opt/ВАША_ГРУППА/ВАШЕ_ИМЯ
# 3. Если папки отсутствует, создать.
# 4. Если папка есть, создать в ней пустой текстовый файл test.txt
# 5. При помощи scp скопировать этот файл себе на компьютер
ssh -i ~/.ssh/id_rsa ec2-user@linux.itcareerhub.de
cd /opt/ВАША_ГРУППА/ВАШЕ_ИМЯ
mkdir /opt/101025-ptm/SMyshynskyi/
touch /opt/101025-ptm/SMyshynskyi/test.txt
date >> /opt/101025-ptm/SMyshynskyi/test.txt
chmod u+x touch /opt/101025-ptm/SMyshynskyi/test.txt
chmod og-r touch /opt/101025-ptm/SMyshynskyi/test.txt
# Выходим с удаленного сервера
exit
# Копируем на свой ПК файл
scp -i ~/.ssh/id_rsa ec2-user@linux.itcareerhub.de:/opt/151223-wde/file.txt "E:/REPO"
# Копируем на свой ПК директорию
scp -r -i ~/.ssh/id_rsa ec2-user@linux.itcareerhub.de:/opt/151223-wde/file.txt "E:/REPO"
# Копируем на свой ПК файл в текущую директорию
scp -i ~/.ssh/id_rsa ec2-user@linux.itcareerhub.de:/opt/151223-wde/file.txt .