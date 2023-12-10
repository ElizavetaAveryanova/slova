from utils import load_random_word
from Player import Player

def main():
    print('Ввведите имя игрока')
    # Получаем у пользователя его имя
    user_name = input().strip().capitalize()
    # Создаем экземпляр класса Player с нужным именем
    player_user = Player(user_name)
    print(f"Привет, {player_user.user_name}!")
    # Вывод полученного рандомного слова
    random_word = load_random_word()
    print(f"Составьте {random_word.count_subswords()} слов из слова {random_word.original_word}")
    print(f"Слова должны быть не короче {len(min(random_word.subswords))} букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите 'stop'")
    print("Поехали, ваше первое слово?")

    while True:
        user_word = input().lower().strip()
        # Если слово stop или стоп, то игра прекращается
        if user_word == 'stop' or user_word == 'стоп':
            break
        # Если слово короче минимальной длины слова из списка наших подслов – это неудачное слово
        elif len(user_word) < len(min(random_word.subswords)):
            print("Слишком короткое слово")
        # Если слово уже было угадано пользователем – это неудачное слово.
        elif player_user.checking_the_used_word_user(user_word):
            print("Уже использовано")
        # Если слова нет в списке допустимых у BasicWord – это неудачное слово
        elif not random_word.checking_the_subwords(user_word):
            print("Неверно")
        else:
            player_user.adds_user_word_in_subwords(user_word)
            print("Верно")
            # Как только количество угаданных слов сравняется с количеством слов, которые можно составить, игра прекращается
            if player_user.count_user_words() == random_word.count_subswords():
                break
    # Выводим количество угаданных слов. Информацию получаем из экземпляра класса Player
    print(f"Игра завершена, вы угадали {player_user.count_user_words()} слов!")

if __name__ == '__main__':
    main()
