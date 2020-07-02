from enum import Enum
import time
import random

WORDS_LIST = ['skillfactory', 'телефон', 'copybook', 'apple', 'orion', 'covid']
MAX_AMOUNT_OF_ATTEMPS = 4
popytki=5

class Result(Enum):
    FAIL = 0
    WIN = 1
    CONTINUE = -1

def choose_word(word_list):
    return random.choice(word_list)

def calculate_score(wrong_guesses):
    return max(MAX_AMOUNT_OF_ATTEMPS - wrong_guesses, 0)


class Game():
    def __init__(self):
        self.answer = choose_word(WORDS_LIST)
        self.guess_count = 0
        self.guessed_letters = []

    def guess(self, letter):
        if not letter.isalpha():
            raise ValueError
        if self.get_result() != Result.CONTINUE:
            raise ValueError
        self.guessed_letters.append(letter)
        if letter.lower() in self.answer:
            return True
        else:
            self.guess_count += 1
            print("осталось "+str(MAX_AMOUNT_OF_ATTEMPS-self.guess_count)+" попыток")
            return False

    def get_current_state(self):
        current_state = []
        for i in self.answer:
            if i in self.guessed_letters:
                current_state.append(i)
            else:
                current_state.append('_')
        return ''.join(current_state)

    def get_result(self):
        if self.guess_count >= MAX_AMOUNT_OF_ATTEMPS:
            return Result.FAIL
        elif self.answer == self.get_current_state():
            return Result.WIN
        else:
            return Result.CONTINUE

def create_game():
    game = Game()
    return game

def next_step(result):
    if result == Result.WIN:
        print("Вы выиграли!")
    elif result == Result.FAIL:
        print("Вы проиграли!!")
    else:
        time.sleep(0.1)
        return True


def cli_gameplay():
    print("Вы должны угадать слово буква за буквой.Ну типа как в Поле Чудес))")
    print("У вас есть только 5(!) неудачных попыток!")
    game = Game()
    print(game.get_current_state())
    while True:
        letter = input()
        try:
            game.guess(letter)
        except ValueError:
            print("Используйте буквы")
        print(game.get_current_state())
        result = game.get_result()
        do_continue = next_step(result)
        if not do_continue:
           return False

if __name__ == '__main__': 
    while True: 
        cli_gameplay()
        