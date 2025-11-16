# 1. Зайти на учебный сервер по адресу linux.itcareerhub.de
# 2. Объявите новую системную переменную ANDREW_VARIABLE и присвойте ей значение с
# именем вашей группы, где вместо ANDREW - будет ваше имя.
# 3. По полному пути /opt/ВАША_ГРУППА/ВАШЕ_ИМЯ создайте файл скрытый файл process_management, в который:
  # a. Запишите дату
  # b. Допишите “Welcome to Amazon server” - любым удобным Вам способом
  # c. Допишите информации об общем объеме оперативной памяти - любым удобным Вам способом
  # d. Допишите в него информацию из списка процессов, но из вывода всей команды взять
  # только КОЛИЧЕСТВО процессов, запущенные под пользователем root
  # e. Допишите информацию об объявленных переменных, но отфильтруйте так, чтобы осталась только Ваша переменная
  # из пункта 2 (В примере ANDREW_VARIABLE)
  # f. * PID и PPID процесса “/usr/sbin/sshd -D” в виде
  # g. PID *** PPID *, где *** и * это актуальные идентификаторы процесса и родительского процесса
# 4. Пришлите получившийся файл или скриншот содержимого или команды, которые вы выполняли.
# 5. Необязательное задание - пришлите команду, с помощью которой Вы можете решить задание.
ssh ec2-user@linux.itcareerhub.de
export SERGEY_VARIABLE=101025-ptm
touch /opt/101025-ptm/SMyshynskyi/.process_management
date >> /opt/101025-ptm/SMyshynskyi/.process_management
echo "Welcome to Amazone server" >> /opt/101025-ptm/SMyshynskyi/.process_management
free -m >> /opt/101025-ptm/SMyshynskyi/.process_management
ps -ef | grep root >> /opt/101025-ptm/SMyshynskyi/.process_management
echo $SERGEY_VARIABLE >> /opt/101025-ptm/SMyshynskyi/.process_management
ps -ef | grep "/usr/sbin/sshd -D" | grep -v grep | awk '{print "PID " $2 " PPID " $3}' >> /opt/101025-ptm/SMyshynskyi/.process_management
unset $SERGEY_VARIABLE
exit
scp ec2-user@linux.itcareerhub.de:/opt/101025-ptm/SMyshynskyi/.process_management "E:/REPO"