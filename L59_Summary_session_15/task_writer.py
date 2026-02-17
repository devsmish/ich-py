def write_to_file(filename='tasks.txt'):
    while True:
        with open(filename, 'a', encoding='utf-8') as file:
            task = input('Введите задачу, "exit" to exit: ').strip()

            if task == 'exit':
                break

            if task:
                file.write(task + '\n')

                print('Задача успешно записана!')

write_to_file('tasks.txt')