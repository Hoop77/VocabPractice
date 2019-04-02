# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

CSV_HEADER = 'english,german,correct,wrong\n'

class VocabEntry:
    def __init__(self, english, german, correct_count, wrong_count):
        self.english = english
        self.german = german
        self.correct_count = correct_count
        self.wrong_count = wrong_count

def read_words(f):
    words = []
    for line in f:
        word = line.strip()
        if word:
            words.append(word)
    return words

def create_vocab():
    with open('german.txt', 'r', encoding='utf8') as file_ger:
        with open('english.txt', 'r', encoding='utf8') as file_eng:
            with open('vocab.csv', 'w', encoding='utf8') as file_vocab:
                words_ger = read_words(file_ger)
                words_eng = read_words(file_eng)
                file_vocab.write(CSV_HEADER)
                for i, word_eng in enumerate(words_eng):
                    word_ger = words_ger[i]
                    file_vocab.write('"{}","{}",0,0\n'.format(word_eng, word_ger))

def read_vocab():
    data = pd.read_csv('vocab.csv')[['english', 'german', 'correct', 'wrong']].values
    vocab = []
    for entry in data:
        vocab.append(VocabEntry(str(entry[0]), str(entry[1]), int(entry[2]), int(entry[3])))
    return vocab

def write_vocab(vocab):
    with open('vocab.csv', 'w', encoding="utf8") as file_vocab:
        file_vocab.write(CSV_HEADER)
        for entry in vocab:
            file_vocab.write('"{}","{}",{},{}\n'.format(entry.english, entry.german, entry.correct_count, entry.wrong_count))

def filter_accomplished(vocab):
    new_vocab = []
    for entry in vocab:
        if entry.correct_count < 1:
            new_vocab.append(entry)
    return new_vocab

def practice(vocab, indices, eng_to_ger):
    for i in range(len(indices)):
        idx = indices[i]
        print('{}/{}'.format(i + 1, len(indices)))
        word_ger = vocab[idx].german
        word_eng = vocab[idx].english
        if eng_to_ger:
            input('\t{}'.format(word_eng))
            print('\t{}'.format(word_ger))
        else:
            input('\t{}'.format(word_ger))
            print('\t{}'.format(word_eng))
        response = ''
        while response not in ['y', 'n', 'q']:
            response = input('Correct? (y/n/q)\n')
        if response == 'q':
            break
        elif response == 'y':
            vocab[idx].correct_count += 1
        elif response == 'n':
            vocab[idx].wrong_count += 1
    return vocab

def practice_random_subset(vocab, eng_to_ger=True):
    num_exercise_words = int(input('Number of words to exercise: '))
    num_words = len(vocab)
    indices = np.array(list(range(num_words)))
    np.random.shuffle(indices)
    indices = indices[:num_exercise_words]
    return practice(vocab, indices, eng_to_ger)

def practice_alphabetically(vocab, eng_to_ger=True):
    num_words = len(vocab)
    key = lambda k: vocab[k].english if eng_to_ger else lambda k: vocab[k].german
    indices = sorted(range(num_words), key=key)
    return practice(vocab, indices, eng_to_ger)

if __name__ == '__main__':
    # create_vocab()
    # exit()
    vocab = read_vocab()
    print('Vocab size: {}'.format(len(vocab)))
    vocab = filter_accomplished(vocab)
    #vocab = practice_alphabetically(vocab)
    vocab = practice_random_subset(vocab)
    write_vocab(vocab)
            
