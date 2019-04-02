# -*- coding: utf-8 -*-
import numpy as np

def read_words(f):
    words = []
    for line in f:
        word = line.strip()
        if word:
            words.append(word)
    return words

def practice_random_subset(words_ger, words_eng, eng_to_ger=True):
    num_exercise_words = int(input('Number of words to exercise: '))
    num_words = len(words_ger)
    indices = np.array(list(range(num_words)))
    np.random.shuffle(indices)

    for i in range(num_exercise_words):
        print('{}/{}'.format(i + 1, num_exercise_words))
        word_ger = words_ger[indices[i]]
        word_eng = words_eng[indices[i]]
        if eng_to_ger:
            input('\t{}'.format(word_eng))
            print('\t{}'.format(word_ger))
        else:
            input('\t{}'.format(word_ger))
            print('\t{}'.format(word_eng))

def practice_alphabetically(words_ger, words_eng, eng_to_ger=True):
    num_words = len(words_ger)
    key = lambda k: words_eng[k] if eng_to_ger else lambda k: words_ger[k]
    indices = sorted(range(num_words), key=key)
    for i in range(num_words):
        print('{}/{}'.format(i + 1, num_words))
        if eng_to_ger:
            input('\t{}'.format(words_eng[indices[i]]))
            print('\t{}'.format(words_ger[indices[i]]))
        else:
            input('\t{}'.format(words_ger[indices[i]]))
            print('\t{}'.format(words_eng[indices[i]]))

if __name__ == '__main__':
    with open('german.txt', 'r', encoding='utf8') as file_ger:
        with open('english.txt', 'r') as file_eng:
            words_ger = read_words(file_ger)
            words_eng = read_words(file_eng)
            practice_alphabetically(words_ger, words_eng)
            
