import pickle
import re

import click
import numpy as np
from textblob import TextBlob


@click.command()
@click.option('--model', required=True)
@click.option('--seed', default='.', required=False)
@click.option('--length', required=True, type=int)
@click.option('--output', default='stdout', required=False)
@click.option('--help', required=False)
def generate(model, seed, length, output, help):
    with open(model, 'rb') as f:
        mod = pickle.load(f)

    if seed in mod.keys():
        first_word = np.random.choice(list(mod[seed].keys()))
    else:
        first_word = np.random.choice(list(mod.keys()))

    test_chain = [first_word]
    res = []
    while len(test_chain) < length:
        res = np.random.choice(list(mod[test_chain[-1]].keys()), 1, True,
                               [float(el) / sum(list(mod[test_chain[-1]].values())) for el in
                                list(mod[test_chain[-1]].values())])
        test_chain.append(res[0])

    sentence = ' '.join(test_chain)
    sentence = re.sub(' \.', '.', sentence)

    if output == 'stdout':
        print(TextBlob(sentence.capitalize()))
    else:
        f = open(output, 'w')
        f.write(sentence)
        f.close()

generate()

