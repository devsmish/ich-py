text = input("Enter a text: ")
print("Содержит 'Python': ", "Python" in text)

# Прямоугольник из символов
shirina = int(input("Введите ширину: "))
vysota = int(input("Введите высоту: "))
for i in range(vysota):

    stroka_simvolov = ""
    for j in range(shirina):
        # Добавляем символ к текущей строке
        stroka_simvolov = stroka_simvolov + "*"

    print(stroka_simvolov)

W = int(input()) # 5
H = int(input())# 3

for i in range(H):
    for j in range(W):
        print('*', end="")
    print()