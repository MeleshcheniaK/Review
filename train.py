import click
from collections import defaultdict
import pickle
import re


# Генератор строк из текста
def strings(name):
    if name == "stdin":
        yield input()
    for string in open(name, 'r', encoding='utf-8'):
        yield string


@click.command()
@click.option('--input-dir', default='stdin')
@click.option('--model')
@click.option('--lc', default=1, required=False)
def train(input_dir, model, lowercase):
    """
    Обучает модель для генерации текста на основе цепей Маркова.
    Файл из которого загружается текстовый источник -- input_dir.
    Файл в который загружается модель -- model.
    :param input_dir: Исходник для обучения.
    :param model: Файл для записи модели.
    :param lc: Приводить ли текст к lowercase.
    """
    chain = defaultdict(lambda: defaultdict(int))
    start = ""

    # Считывание текста из файла
    for string in strings(input_dir):
        # Приведение текста к lowercase
        if lowercase:
            string = string.lower()

        # Чистка строки от лишних символов
        string = re.sub(' +', ' ', string)
        string = re.sub('\.+|\?|!', ' .', string)
        string = re.sub('[,()]', ' ', string)
        string = string[:-1]
        line = [start] + re.split('; |, | ', string)

        # Создание словаря из пар слов
        for i in range(len(line) - 1):
            chain[line[i]][line[i + 1]] += 1

        # Сохранение последнего слова для новой линии
        if len(line) > 0:
            start = line[-1]

    # Запись модели в файл
    with open(model, 'wb') as output:
        pickle.dump(chain, output)

# Вызов функции
train()
