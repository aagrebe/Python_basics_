import os
path = os.getcwd()

try:
    with open(os.path.join(path, "text_2.txt")) as my_words:
        text_words = my_words.read()
        print(text_words)
        text_change = text_words.replace('\n', ' ')
        words = text_change.split(" ")
    with open(os.path.join(path, "text_2.txt")) as my_lines:
        text_lines = my_lines.readlines()
        number = len(text_lines)
except IOError:
    print("Произошла ошибка ввода-вывода!")
print(f"В стихотворении количество строк - {number}, количество слов - {len(words)}")