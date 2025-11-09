# генерация ключей
ssh-keygen -C EMAIL
# Подключение к серверу
ssh -i ~/.ssh/id_rsa ec2-user@linux.itcareerhub.de
# Создать свою директорию
mkdir -p /opt/101025-ptm/ВАШЕ_ИМЯ
# другие команды
cd /opt/101025-ptm/SMyshynskyi/
ls -la | tail -n +4 | wc -l
history >> sshkeypract.sh && export_file sshkeypract.sh
scp ec2-user@linux.itcareerhub.de:/opt/101025-ptm/SMyshynskyi/TestDir/sshkeypract.sh E:\Drawio\sshkeypract.sh
cat /opt/101025-ptm/SMyshynskyi/TestDir/sshkeypract.sh