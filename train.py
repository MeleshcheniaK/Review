import click
import copyreg
import dill
import re
import sys

from collections import defaultdict


# Получение строк из текста
def get_strings(name):
    if name == 'stdin':
        for string in sys.stdin:
            yield string
    else:
        with open(name, 'r', encoding='utf-8') as input:
            for string in input:
                yield string


# Чистка строки от лишних символов
def clean(string):
    string = re.sub(' +', ' ', string)
    string = re.sub('\.+|\?|!', ' .', string)
    string = re.sub('[,()]', ' ', string)
    string = string[:-1] # Удаление символа \n
    string = re.split('; |, | ', string)
    return string


@click.command()
@click.option('--input-dir', default='stdin')
@click.option('--model')
@click.option('--lc', default=1, required=False)
def train(input_dir, model, lc):
    """
    Обучает модель для генерации текста на основе цепей Маркова.
    Файл из которого загружается текстовый источник -- input_dir.
    Файл в который загружается модель -- model.
    :param input_dir: Исходник для обучения.
    :param model: Файл для записи модели.
    :param lc: Приводить ли текст к lowercase.
    """
    chain = defaultdict(lambda: defaultdict(int))
    start = ''

    # Считывание текста из файла
    for string in get_strings(input_dir):
        # Приведение текста к lowercase
        if lc:
            string = string.lower()

        line = clean(string)

        # Создание словаря из пар слов
        for i in range(len(line) - 1):
            chain[line[i]][line[i + 1]] += 1

        # Сохранение последнего слова для новой линии
        if len(line) > 0:
            start = line[-1]

    # Запись модели в файл
    with open(model, 'wb') as output:
        dill.dump(chain, output)


# Вызов функции
train()
