def write_to_file(filename='tasks.txt'):
    with open(filename, 'a', encoding='utf-8') as file:
        while True:
            task = input('Введите задачу, "exit" to exit: ')
            if task == 'exit':
                break
            file.write(task + '\n')
            print('Задача успешно записана!')

write_to_file('tasks.txt')