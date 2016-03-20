__author__ = 'Tony Cheng'

import random


class Player(object):
    def __init__(self, name):
        self._name = name
        self._score = 0

    def reset_score(self):
        self._score = 0

    def incr_score(self):
        self._score += 1

    def get_name(self):
        return self._name

    def get_move(self):
        pass

    def __str__(self):
        # return 'name = %s , score = %d' % (self._name, self._score)
        return '%s %s' % (self.__class__, self.get_name())

    def __repr__(self):
        # return 'Player %s' % self.get_name()
        return '%s %s' % (self.__class__, self.get_name())


class Human(Player):
    def get_move(self):
        while True:
            try:
                n = int(raw_input('%s move 1-10 : ' % self.get_name()))
                if 1 <= n <= 10:
                    return n
                else:
                    print('Oops!')
            except Exception():
                print('Exception: Oops!')


class Computer(Player):
    # def __repr__(self):
    #    return 'Computer %s' % self.get_name()

    def get_move(self):
        return random.randint(1, 10)


def play_undercut(p1, p2):
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    print '%s move: %d' % (p1.get_name(), m1)
    print '%s move: %d' % (p2.get_name(), m2)
    if m1 == m2 - 1:
        p1.incr_score()
        return p1, p2, '%s wins!' % p1.get_name()
    elif m2 == m1 - 1:
        p2.incr_score()
        return p1, p2, '%s wins!' % p2.get_name()
    else:
        return p1, p2, 'draw: no winner'


def main():
    while True:
        print play_undercut(Computer('ThinkPad'),  Human('Tony'))

if __name__ == '__main__':
    main()
