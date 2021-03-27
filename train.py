import pickle
import re

import click


def lines(name):
    if name == "stdin":
        yield input()
    for f in open(name, 'r', encoding='utf-8'):
        yield f


def update(dictionary, item):
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1


@click.command()
@click.option('--input-dir', default='stdin')
@click.option('--model')
@click.option('--lc', default=1, required=False)
@click.option('--help', required=False)
def train(input_dir, model, lc, help):
    chain = {}
    start = ""

    for f in lines(input_dir):
        if lc:
            f = f.lower()
        f = re.sub(' +', ' ', f)
        f = re.sub('\.+|\?|!', ' .', f)
        f = re.sub('[,()]', ' ', f)
        f = f[:-1]
        line = [start] + re.split('; |, | ', f)
        while '' in line:
            line.remove('')
        for i in range(len(line) - 1):
            if line[i] in chain:
                update(chain[line[i]], line[i + 1])
            else:
                chain[line[i]] = {line[i + 1]: 1}
        if len(line) > 0:
            start = line[-1]

    with open(model, 'wb') as output:
        pickle.dump(chain, output)

train()
