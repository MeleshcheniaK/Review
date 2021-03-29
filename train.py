import click
from collections import defaultdict
import pickle
import re


# Генератор линий из текста
def lines(name):
    if name == "stdin":
        yield input()
    for line in open(name, 'r', encoding='utf-8'):
        yield line


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
    chain = defaultdict(defaultdict(lambda: 0))
    start = ""

    # Считывание текста из файла
    for string in lines(input_dir):
        # Приведение текста к lowercase
        if lc:
            string = string.lower()

        # Чистка линии от лишних символов
        string = re.sub(' +', ' ', string)
        string = re.sub('\.+|\?|!', ' .', string)
        string = re.sub('[,()]', ' ', string)
        string = string[:-1]
        line = [start] + re.split('; |, | ', string)

        # Создание словаря из пар слов
        for i in range(len(line) - 1):
            if line[i] in chain:
                chain[line[i]][line[i + 1]] += 1
            else:
                chain[line[i]] = {line[i + 1]: 1}

        # Сохранение последнего слова для новой линии
        if len(line) > 0:
            start = line[-1]

    # Запись модели в файл
    with open(model, 'wb') as output:
        pickle.dump(chain, output)

# Вызов функции
train()

