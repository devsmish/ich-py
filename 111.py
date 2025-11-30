text = input("Enter your text: ")
tmp_text = ''
count = 0
for char in text:
    if char.lower() not in tmp_text and char != ' ':
        tmp_text += char.lower()
        count += 1
if count == 26:
    print("Панограмма? True")
else:
    print("Панограмма? False")