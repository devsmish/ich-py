# просмотр системных переменных
env
# обращение к переменной
echo $PATH
echo $LANG
echo $TZ
echo $PWD
# объявление новой переменной
export MY_VAR=hello
export var=world
echo $MY_VAR $var
hello world
# удаление системной переменной
unset MY_VAR
# добавление новой директории в переменную PATH
export PATH=$PATH:/root
# динамическое отслеживание процессов
top
ps -ef
ps aux
ps -ef | grep ssh
kill PID
kill 23034
killall <process_name>
kill -15 PID
kill -9 PID
kill -2 PID
kill -3 PID
df -h
free -m
cat /etc/os-release
cat /proc/cpuinfo
# описание ядра ОС
uname -a
# все зарегистрированные пользователи в системе
w
# Задание
# 1. На сервере найти и отфильтровать все процессы ssh.
# 2. Найдя их, выбрать PID процесса и остановить его при помощи команды kill. Вы остановите ssh сессию
# пользователя, тем самым отключив кого-то от сервера.
ps -aux | grep ssh
kill 4881