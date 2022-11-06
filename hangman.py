#coding python hangman

import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'APPLE', 'POTATOE', 'CARROT', 'LETTUCE', 'BEATROOT', 'PINEAPPLE',
    'PEACH', 'BANANA', 'ORANGE', 'BLUEBERRY', 'STRAWBERRY'
]

class Hangman():
    def __init__(self, guess_word):
        self.fails = 0
        self.guess_word = guess_word
        self.progress = list('_' * len(self.guess_word))
        
    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.guess_word) if letter == char]