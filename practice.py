# -*- coding: utf-8 -*-
import numpy as np

def read_words(f):
    words = []
    for line in f:
        word = line.strip()
        if word:
            words.append(word)
    return words

def practice(words_ger, words_eng, eng_to_ger=True):
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

if __name__ == '__main__':
    with open('german.txt', 'r', encoding='utf8') as file_ger:
        with open('english.txt', 'r') as file_eng:
            words_ger = read_words(file_ger)
            words_eng = read_words(file_eng)
            practice(words_ger, words_eng)
            
