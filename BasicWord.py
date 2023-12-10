class BasicWord:
    def __init__(self, original_word, subswords):
        self.original_word = original_word.upper()
        self.subswords = subswords

    def __repr__(self):
        return f"{self.original_word}:{self.subswords}"

    def checking_the_subwords(self, user_word):
        """
        Метод проверки введенного слова пользователем в списке допустимых подслов
        :param user_word: слова пользователя
        :return: True (есть в списке допустимых слов) /False (нет в списке допустимых слов)
        """
        return user_word in self.subswords

    def count_subswords(self):
        """
        Метод подсчета количества допустимых подслов
        :return: Длину списка допустимых подслов
        """
        return len(self.subswords)



