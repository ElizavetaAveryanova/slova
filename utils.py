import requests
from random import choice
from BasicWord import BasicWord

def load_random_word():
    """
    Функция, которая получает список слов с внешнего ресурса
    выбирает случайное слово из этого списка слов
    создаст экземпляр класса BasicWord
    :return: экземпляр класса BasicWord с рандомным словом и к нему списком допустимые подслова
    """
    list_words = requests.get('https://www.jsonkeeper.com/b/L00D').json()
    random_word = choice(list_words)
    basic_word = BasicWord(random_word['word'], random_word['subwords'])
    return basic_word

