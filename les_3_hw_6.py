def int_func (word):
    first_char = ord(word[0])
    if first_char >= 1072 and first_char <= 1103 or first_char >= 97 and first_char <= 122:
        replace_char = chr(first_char - 32)
        word_list = list(word)
        word_list[0] = replace_char
        word_rep = (''.join(word_list))
        return word_rep
    else: print('Слово должно начинаться с буквы')
"""
Первая часть задания
"""
input_word = input('Введите любое слово: ')
word = input_word.lower()
word_rep = int_func(word)
print(word_rep)
"""
Вторая часть задания
"""
input_sentence = input('Введите неколько слов, разделенных пробелами: ')
sentence = input_sentence.lower()
sentence = sentence.split(' ')
sentence_list = []
for index in range(len(sentence)):
    word_rep_sentence = int_func(sentence[index])
    sentence_list.append(word_rep_sentence)
sentence_rep = (' '.join(sentence_list))
print(sentence_rep)