'''Вы хотите узнать, можно ли пойти гулять.
Условия: (погода хорошая или день выходной) и у вас есть свободное время.'''
good_weather = True
is_weekend = False
free_time = True
can_go_out = (good_weather or is_weekend) and free_time
print(can_go_out) # Резулþтат: True