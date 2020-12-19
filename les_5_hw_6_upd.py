import os
path = os.getcwd()

sum_subject = 0
subject_dict = {}
try:
    with open(os.path.join(path, "subjects_6.txt")) as f:
        text = f.read()
        text_list = [el.split(' ') for el in text.split('\n')]
        print(text_list)
        for el in text_list:
            for i in range(1, 4):
                number = el[i].find('(')
                if number != -1:
                    sum_subject += int(el[i][:number])
                    subject_dict.update({el[0]: sum_subject})
            sum_subject = 0
    print(subject_dict)
except IOError:
    print("Произошла ошибка ввода-вывода!")