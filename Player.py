class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_words = []

    def __repr__(self):
        return (f"Имя пользователя: {self.user_name}\n"
                f"Слова пользователя: {self.user_words}")

    def count_user_words(self):
        """
        Метод получения количества использованных слов пользователем
        :return: Длину списка слов, которые ввел пользователь
        """
        return len(self.user_words)

    def adds_user_word_in_subwords(self, user_word):
        """
        Метод, который добавляет слова введенные пользователем в использованные слова
        :param user_word: слово пользователя
        """
        self.user_words.append(user_word)

    def checking_the_used_word_user(self, user_word):
        """
        Метод, в котором идет проверка использования слова пользователя до этого
        :return: True (использовал до этого) / False (не использовал)
        """
        return user_word in self.user_words

