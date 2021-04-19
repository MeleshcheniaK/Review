import click
import dill
import global_names
import numpy as np
import re

from textblob import TextBlob


@click.command()
@click.option('--model', required=True)
@click.option('--seed', default='', required=False)
@click.option('--length', required=True, type=int)
@click.option('--output', default='stdout', required=False)
def generate(model, seed, length, output):
    """
    Функция генерирует последовательность слов длины length.
    Словарь находится в model.
    Начальное слово -- seed.
    Результат выводится в output(по умолчанию stdout).
    :param model: Файл со словарём
    :param seed: Начальное слово
    :param length: Длина генерируемой последовательности
    :param output: Файл для вывода
    """

    # Загрузка модели из файла
    with open(model, 'rb') as stdin_file:
        working_model = dill.load(stdin_file)

    # Выбор начального слова
    if seed in working_model.keys():
        first_word = seed
    else:
        print("Слово", seed, "не найдено! Включен автоподбор.")
        first_word = np.random.choice(list(working_model.keys()))

    res = []
    chain = [first_word]

    # Создание цепи нужной длины(по одному слову)
    while len(chain) < length:
        next_words = list(working_model[chain[-1]].keys())
        next_words_counts = list(working_model[chain[-1]].values())
        next_words_frequency = [float(count) / sum(next_words_counts) for count in next_words_counts]
        res = np.random.choice(range(len(next_words)), 1, True, next_words_frequency)
        chain += next_words[res[0]]

    # Объединение слов в текст
    sentence = ' '.join(chain)
    sentence = re.sub(' \.', '.', sentence)

    point_index = sentence.find('.')
    # Большая буква в начале предложения
    while -1 < point_index < len(sentence) - global_names.SHIFT:
        first_sentence_letter = sentence[point_index + global_names.SHIFT].upper()
        sentence = sentence[:point_index + global_names.SHIFT] + first_sentence_letter + sentence[point_index + global_names.SHIFT + 1:]
        point_index = sentence.find('.', point_index + global_names.SHIFT)

    # Первый символ - большая буква
    sentence = sentence[0].upper() + sentence[1:]
    # Вывод в файл из stdout
    if output == 'stdout':
        print(TextBlob(sentence))
    else:
        with open(output, 'w') as file:
            file.write(sentence)


# Вызов функции
generate()

