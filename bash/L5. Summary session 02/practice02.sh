   0 echo "Hello, World!" > output.txt
   1 cat output.txt
   2 echo "This is a practice file." >> output.txt
   3 cat output.txt
   4 df
   5 df >> disk_space.txt
   6 cat disk_space.txt 
   7 echo "This is a text line." >> output.txt
   8 tail -3 output.txt >> last_lines.txt
   9 cat last_lines.txt 
  10 wc --help
  11 wc -wlm last_lines.txt >> word_count.txt
  12 touch password_copy.txt
  13 cat word_count.txt 
  14 cat /etc/passwd
  15 cat /etc/passwd >> password_copy.txt 
  16 mv password_copy.txt passwd_copy.txt 
  17 cat passwd_copy.txt 
  18 wc -l passwd_copy.txt 
  19 head -10 passwd_copy.txt >> passwd_head_tail
  20 cp passwd_head_tail /home/passwd_head_tail
  21 tail -4 passwd_copy.txt >> /home/passwd_head_tail
  22 touch result_file.txt
  23 cat output.txt >> result_file.txt 
  24 cat disk_space.txt >> result_file.txt
  25 cat last_lines.txt >> result_file.txt
  26 cat word_count.txt >> result_file.txt
  27 cat passwd_copy.txt >> result_file.txt
  28 cat /home/passwd_head_tail >> result_file.txt 
  29 wc -l result_file.txt 
  30 wc result_file.txt 
  31 df -h
  32 history >> practice02.sh && export_file practice02.sh
