def inp_string():
    global text
    string = input("Введите данные или пустую строку для выхода:")
    text.append(string)
    if not string:
        return
    return "\n".join(text)
text=[]
try:
    with open("text_input_1.txt", "w") as f_obj:
        while True:
            try:
                f_obj.writelines(inp_string())
            except TypeError:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")