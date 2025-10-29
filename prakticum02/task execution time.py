'''Напишите программу, которая запрашивает у пользователя количество задач и среднее время выполнения
одной задачи (в минутах). Программа должна вывести общее время выполнения всех задач в формате часов и
минут.
Пример вывода:
Введите количество задач: 5
Введите среднее время выполнения одной задачи (мин): 40
Общее время: 3 часа и 20 минут'''
task_counts = int(input("Enter the number of your tasks: "))
average_time = int(input("Enter the average solution time (in minutes): "))

total_time = task_counts * average_time
print("Общее время:", str(total_time // 60), "часа и", str(total_time % 60), "минут")

# альтернативный вариант
tasks = int(input("Введите количество задач: "))
time_per_task = int(input("Введите среднее время выполнения одной задачи (мин): "))
total_minutes = tasks * time_per_task
hours = total_minutes // 60
minutes = total_minutes % 60
print("Общее время:", hours, "часа и", minutes, "минут")