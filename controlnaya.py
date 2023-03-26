#Задание массива слов
input_array = ['Hello', '2', 'World', ':-)']
#Массив для коротких слов
short_words = []

#Запись коротких слов из исходного массива
for word in input_array:
    if len(word) <= 3:
        short_words.append(word)

#Вывод слов из массива коротких слов
print(short_words)
