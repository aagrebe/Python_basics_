import os
path = os.getcwd()

text_replace = ["Один", "Два", "Три", "Четыре"]
text_changes = []

try:
    with open(os.path.join(path, "one_four_4.txt")) as f_obj:
        text = f_obj.read()
        text_change = [el.split(" ") for el in text.split("\n")]
        for i in range(len(text_change)):
            text_change[i][0] = text_replace[i]
            text_changes.append(" ".join(text_change[i]))
    text_changes = "\n".join(text_changes)
    print(text_changes)

    with open(os.path.join(path, "один_четыре_4.txt"), "w") as f_obj:
        f_obj.writelines(text_changes)
except IOError:
    print("Произошла ошибка ввода-вывода!")