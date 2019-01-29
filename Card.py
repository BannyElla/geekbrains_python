import random
class Row:
    __row = []
    __zero = " "
    __x = "X"

    def __init__(self, card_row):
         card_row.sort()
         for i in range(0, 4):
             ind = random.randint(0, 4)
             card_row[ind : ind] = self.__zero
         self.__row = card_row

    @property
    def card_row(self):
        from functools import reduce

        return reduce(lambda x, y: "{:2} {:2}".format(x, y), self.__row)

        # return self.__row

    def zeroize(self, element):
        if(element in self.__row):
            index = self.__row.index(element)
            self.__row[index] = self.__x

    def count_x(self):
        return len(list(filter(lambda a: a == self.__x, self.__row)))

    def get_first_digit(self):
        return self.__row[0]

    def get_row(self):
        return self.__row

    def check_digit(self, digit):
        if digit in self.__row:
            self.zeroize(digit)
            return True
        else:
            return False


class Card():
    __rows = []

    def __init__(self, start, end):
        digits_list = []
        while len(digits_list) < 25:
            digit = random.randint(start, end + 1)
            if digit not in digits_list:
                digits_list.append(digit)

        random.shuffle(digits_list)
        self.__rows = [Row(digits_list[i : i + 5]) for i in range(0, 25, 5)]

    def __str__(self):
        line = "-" * 26
        string = ""
        for row in self.__rows:
            string += row.card_row + "\n"
        return "{}{}\n".format(string, line)

    def count_x(self):
        count = 0
        for row in self.__rows:
            count += row.count_x()
        return count

    def get_first_digit(self):
        return self.__rows[0].get_first_digit()

    def check_digit(self, digit):
        check = False
        for row in self.__rows:
            if row.check_digit(digit):
                check = True
                break
        return check



    @property
    def rows(self):
        return self.__rows

class Player:
    _name = ""
    def __init__(self, card):
        self.card = card

    def did_i_win(self, step):
        print("{}: {}".format(self.get_name(), self.card.count_x()))
        if self.card.count_x() == step:
            return True
        else:
            return False

    def get_name(self):
        return self._name



class Computer(Player):
    _name = "Компьютер"

    def action(self, digit):
        self.card.check_digit(digit)



class User(Player):
    _name = "Пользователь"
    def action(self, digit):
        return self.card.check_digit(digit)

def next_bochonok():
    rnd = random.randint(1, 90)
    if rnd not in used_bochonok:
        used_bochonok.append(rnd)
        return rnd
    else:
        next_bochonok()


bochonok = 90
step_for_win = 2
used_bochonok = []
win = False
winner = "Никто не одержал победу"
computer_card = Card(1, 90)
computer = Computer(computer_card)
user_card = Card(1, 90)
user = User(user_card)

print("START!")
while (not win and bochonok > 0):
    random_digit = next_bochonok()
    bochonok -= 1

    print("Новый бочонок: {} (осталось {})".format(random_digit, bochonok))
    print("------ Ваша карточка -----")
    print(user_card)
    print("-- Карточка компьютера ---")
    print(computer_card)
    print("Использованные бочонки: {}".format(used_bochonok))
    computer.action(random_digit)

    responce = input("Зачеркнуть цифру? (y/n) ")
    check = user.action(random_digit)
    if (responce == "n".lower() and check) or (responce == "y".lower() and not check):
        win = True
        winner = computer.get_name()
        break

    user_win = user.did_i_win(step_for_win)
    comp_win = computer.did_i_win(step_for_win)
    if user_win and comp_win:
       winner = "Ничья"
       win = True
    elif user_win:
        winner = "Победил {}".format(user.get_name())
        win = True
    elif comp_win:
        winner = "Победил {}".format(computer.get_name())
        win = True
    print()

if win:
    print(winner)
else:
    print("Никто не выиграл")

