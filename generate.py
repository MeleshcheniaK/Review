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
    with open(model, 'rb') as file:
        mod = dill.load(file)

    # Выбор начального слова
    if seed in mod.keys():
        first_word = seed
    else:
        first_word = np.random.choice(list(mod.keys()))

    res = []
    test_chain = [first_word]

    # Создание цепи нужной длины(по одному слову)
    while len(test_chain) < length:
        next_words = list(mod[test_chain[-1]].keys())
        next_words_counts = list(mod[test_chain[-1]].values())
        next_words_frequency = [float(count) / sum(next_words_counts) for count in next_words_counts]
        res = np.random.choice(range(len(next_words)), 1, True, next_words_frequency)
        test_chain += next_words[res[0]]

    # Объединение слов в текст
    sentence = ' '.join(test_chain)
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
