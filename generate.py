import click
import numpy as np
import pickle
import re
from textblob import TextBlob

#Обработка флагов
@click.command()
@click.option('--model', required=True)#Путь к файлу, из которого загружается модель
@click.option('--seed', default='.', required=False)#необязательный аргумент. Начальное слово. Если не указано, слово выбирается случайно из всех слов (не учитывая частоты).
@click.option('--length', required=True, type=int)#Длина генерируемой последовательности
@click.option('--output', default='stdout', required=False)#Необязательный аргумент. Файл, в который будет записан результат. Если аргумент отсутствует, вывод производиться в stdout
def generate(model, seed, length, output):
    #Загрузка модели из файла 	
    with open(model, 'rb') as f:
        mod = pickle.load(f)
    
    #Выбор первого слова	
    if seed in mod.keys():
        first_word = np.random.choice(list(mod[seed].keys()))
    else:
        first_word = np.random.choice(list(mod.keys()))

    res = []
    test_chain = [first_word]
    
    #Создание цепи нужной длины(по одному слову)    
    while len(test_chain) < length:
    	words = list(mod[test_chain[-1]].values())
    	probability = [float(el) / sum(words) for el in words]
        res = np.random.choice(words, 1, True, probability)
        test_chain.append(res[0])

    #Объединение слов в текст
    sentence = ' '.join(test_chain)
    sentence = re.sub(' \.', '.', sentence)

    #Вывод в файл из stdout
    if output == 'stdout':
        print(TextBlob(sentence.capitalize()))
    else:
    	with open(output, 'w') as f 
            f.write(sentence)
            f.close()

#Вызов функции
generate()
