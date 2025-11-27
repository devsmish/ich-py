# # Форматирование строки и целого числа
# name = "Alice"
# age = 30
# text = "My name is %s and I am %d years old." % (name, age)
# print(text)
#
# # Форматирование числа с плавающей точкой
# pi = 3.14159
# text = "The value of pi is approximately %.2f." % pi
# print(text)
# print(pi)

# name = "Alice"
# age = 30
# text = "My name is {} and I am {} years old."
# print(text.format(name, age))
# print(text.format(age, name))

# text = "My name is {name} and I am {age} years old. Are you also {age} years old?"
# # print(text.format(name="Bob", age=25))
# name = "Alice"
# print(text.format(name=name, age=25))
# print(text.format(name="Bob", age=22))
# print(text.format(name=name, age=33))

# text = "Her name is {1} and she is {0} years old. {1} loves Python."
# print(text.format(28, "Anna"))

# text = "The {0} is {color}."
# print(text.format("sky", color="blue"))
# # print(text.format(color="blue", "sky"))  # error

# name = "Alice"
# age = 25
# text = f"My name is {name} and I am {age + 1} years old."
# name2 = "Bob"
# text2 = f"My name is {name2} and I am {age + 10} years old."
# print(text)
# print(text2)

# x = 10
# y = 20
# text = f"The sum of {x} and {y} is {x + y}."
# print(text)

# text = "Python"
# text_info = f"The length of '{text}' is {len(text)} and its uppercase version is {text.upper()}."
# print(text_info)

# name = "Charlie"
# age = 30
# text = f"""Info
# Name: {name}
# Age: {age}
# """
# print(text)
#
# print(text.format(name="Tanya", age=31))


# pi = 3.115
# # f-строки
# text_fstring = f"Pi rounded to 2 decimal places is {pi:.2f}"
# # Метод format()
# text_format1 = "Pi rounded to 2 decimal places is {:.2f}".format(pi)
# text_format2 = "Pi rounded to 2 decimal places is {0:.2f}".format(pi)
# text_format3 = "Pi rounded to 2 decimal places is {num:.2f}".format(num=pi)
# print(text_fstring)
# print(text_format1)
# print(text_format2)
# print(text_format3)
#
# large_number = 5473724534524575.6457
# # f-строки
# text_fstring = f"The number with thousand separators: {large_number:,}"
# # Метод format()
# text_format = "The number with thousand separators: {:,}".format(large_number)
# print(text_fstring)
# print(text_format)


# f-строки
# text_fstring = f"start_{'text':<10}_end"
# # Метод format()
# text_format = "start_{:>10}_end"
# print(text_fstring)
# print(f"start_{'text':^10}_end")
# print(text_format.format("text"))

# number = 40
# text = 'hi'
# # f-строки
# text_fstring = f"start_{number:5}_end"
# # Метод format()
# text_format = "start_{:5}_end"
# print(text_fstring)
# print(text_format.format(text))
#
# # Заполнение нулями
# number = 40
# print(f"{number:0>5}")
# print(f"{345:0>5}")
# print(f"{1:0>5}")
#
# # Заполнение нижним подчеркиванием
# print(f"{'Python':_^10}")
# print(f"{'Pythn':_^10}")


text = "Python"

# ljust(): выравнивание по левому краю
print(text.ljust(15))
print(text.ljust(15, '-'))
# rjust(): выравнивание по правому краю
print(text.rjust(15))
print(text.rjust(15, '-'))
# center(): выравнивание по центру
print(text.center(15))
print(text.center(15, '-'))
