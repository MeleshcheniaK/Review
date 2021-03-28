import click
from collections import defaultdict
import pickle
import re


#Генератор линий из текста
def lines(name):
    if name == "stdin":
        yield input()
    for f in open(name, 'r', encoding='utf-8'):
        yield f

#Обновление словаря
def update(dictionary, item):
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1


@click.command()
#Путь к файлу. Если данный аргумент не задан, тексты будут вводятся из stdin.
@click.option('--input-dir', default='stdin')
#Путь к файлу, в который сохраняется модель.
@click.option('--model')
#При задании приводит тексты к lowercase.
@click.option('--lc', default=1, required=False)
def train(input_dir, model, lc):
    chain = defaultdict(defaultdict(lambda: 0))
    start = ""
    
    #Считывание текста из файла 
    for f in lines(input_dir):
        #Приведение текста к lowercase
        if lc:
            f = f.lower()
            
        #Чистка линии от лишних символов    
        f = re.sub(' +', ' ', f)
        f = re.sub('\.+|\?|!', ' .', f)
        f = re.sub('[,()]', ' ', f)
        f = f[:-1]
        line = [start] + re.split('; |, | ', f)
            
        #Создание словаря из пар слов    
        for i in range(len(line) - 1):
            if line[i] in chain:
                chain[line[i]][line[i + 1]] += 1
            else:
                chain[line[i]] = {line[i + 1]: 1}
        
        #Сохранение последнего слова для новой линии
        if len(line) > 0:
            start = line[-1]
    
    #Запись модели в файл
    with open(model, 'wb') as output:
        pickle.dump(chain, output)

#Вызов функции
train()
