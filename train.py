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
    string = re.sub('\.+|\?|!', ' ', string)
    string = re.sub('[,()]', ' ', string)
    string = string[:-1]
    string = string[:-1]  # Удаление символа \n
    string = re.sub(' +', ' ', string)
    string = string[:-1] # Удаление символа \n
    string = re.split('; |, | ', string)
    return string


@click.command()
@click.option('--input-dir', default='stdin')
@click.option('--model')
@click.option('--lc', default=1, required=False)
@click.option('--ngram', default=2, required=False)
def train(input_dir, model, lc, ngram):
    """
    Обучает модель для генерации текста на основе цепей Маркова.
    Файл из которого загружается текстовый источник -- input_dir.
    Файл в который загружается модель -- model.
    :param input_dir: Исходник для обучения.
    :param model: Файл для записи модели.
    :param lc: Приводить ли текст к lowercase.
    :param ngram: Для построения n-граммных моделей
    """
    chain = defaultdict(lambda: defaultdict(int))
    start = ""
    start = []
    start = ''

    # Считывание текста из файла
    for string in get_strings(input_dir):
        # Приведение текста к lowercase
        if lc:
            string = string.lower()
        
        # Создание строки для обработки (первое слово это конец предыдущей строки или пустой элемент, если строка первая)
        line = [start] + clean(string)

        # Создание строки для обработки (первое слово это конец предыдущей строки или пустой элемент, если строка первая)
        line = start + clean(string)

        # Создание словаря из пар слов
        for i in range(len(line) - ngram):
            test_tuple = tuple([line[j+i] for j in range(1, ngram + 1)])
            chain[line[i]][test_tuple] += 1

        # Сохранение последних слов для новой линии
        start = line[-1 * (min(len(line), ngram)-1)::]

    # Запись модели в файл
    with open(model, 'wb') as output:
        dill.dump(chain, output)


# Вызов функции
train()
