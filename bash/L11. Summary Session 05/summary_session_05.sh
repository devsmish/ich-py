# Разбор домашнего задания из L10
export ANDREW_VARIABLE=my_group
date >> /opt/GROUP/NAME/.process_management
echo “Welcome to Amazon server” >> /opt/GROUP/NAME/.process_management
free -m | grep Mem | awk {'print $2'} - или просто 2 GB текстовым редактором
ps -ef | grep root | grep -v grep --color=auto | wc -l - идеально
ps -ef | grep root | wc -l - хорошо, но в список процессов попадает ec2-user 16546 16220 0 16:30 pts/0 иди ps -U 1
00:00:00 grep --color=auto root, его надо пропустить
env | grep ANDREW >> /opt/GROUP/NAME/.process_management
ps -ef | grep "/usr/sbin/sshd -D" | grep -v grep | awk '{print "PID", $2, "PPID", $3}' >>
/opt/GROUP/NAME/.process_management
# Задание
# 1. Подсчитаем количество процессов ssh на учебном сервере
# 2. При подсчете не забываем не учитывать сам процесс grep
# 3. В /var/log/messages поищите и посчитайте количество ошибок (Error, ERROR )
# 4. Перенаправьте строки с ошибками из /var/log/messages в новый файл для дальнейшего анализа
# 5. Откройте полученный файл в текстовом редакторе и попробуйте удалить из него несколько строк
# 6. Сохраните файл
ps -ef | grep ssh | wc -l
ps -ef | grep ssh | grep -v grep | wc -l >> /opt/101025-ptm/SMyshynskyi/count-ssh.txt
cat /opt/101025-ptm/SMyshynskyi/count-ssh.txt
grep Error /var/log/messages | wc -l
grep -i "Error" /var/log/messages | wc -l
cat /var/log/messages | grep Error | wc -l
cat /var/log/messages | grep ERROR | wc -l
grep -i "Error" /var/log/messages >> /opt/101025-ptm/SMyshynskyi/count-ssh.txt
vi /opt/101025-ptm/SMyshynskyi/count-ssh.txt
exit
scp ec2-user@linux.itcareerhub.de:/opt/101025-ptm/SMyshynskyi/count-ssh.txt "E:/REPO/"