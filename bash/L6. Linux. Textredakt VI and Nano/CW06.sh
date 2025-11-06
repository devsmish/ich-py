   0 cd /tmp
   1 touch file.txt
   2 vi /tmp/file.txt
   3 date >> /tmp/file.txt 
   4 cat /tmp/file.txt 
   5 vi /tmp/file.txt
   6 cat /tmp/file.txt 
   7 vi /tmp/file.txt
   8 cat /tmp/file.txt 
   9 history >> CW06.sh && export_file CW06.sh
  10 cd /home
  11 touch text_editors.txt
  12 vi /home/text_editors.txt 
  13 nano /home/text_editors.txt 
  14 cat /home/text_editors.txt 
  15 df -h
  16 df -h | grep -w | awk {'print $5'} | sed 's/%//'
  17 cd /root
  18 mkdir -p test3
  19 touch /root/test3/myfile.txt
  20 df -h >> /root/test3/myfile.txt 
  21 cat /root/test3/myfile.txt 
  22 ls -la / | head -n 9 >> /root/test3/myfile.txt 
  23 cat /root/test3/myfile.txt 
  24 tail -n 3 /etc/group | wc -m >> /root/test3/myfile.txt 
  25 cat /root/test3/myfile.txt 
  26 history >> CW06.sh && export_file CW06.sh
