from player1 import Player as Player1
from player2 import Player as Player2


class Game:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]

    def __init__(self):
        self.data = [[0 for i in range(8)] for i in range(8)]
        self.data[4][3] = 1
        self.data[3][4] = 1
        self.data[3][3] = 2
        self.data[4][4] = 2

    def stone_to_char(self, stone):
        return {0: '  ', 1: '● ', 2: '○ '}[stone]

    def show(self):
        print('■ ' * 10)
        for i in range(8):
            print('■ ', end='')
            for j in range(8):
                print(self.stone_to_char(self.data[i][j]), end='')
            print('■ ')
        print('■ ' * 10)

    def in_range(self, x, y):
        return x in range(8) and y in range(8)

    def can_flip_in_direction(self, player, x, y, i, j):
        if (player, x, y) == (1, 1, 2):
            pass
        cx, cy = x + i, y + j
        if not self.in_range(cx, cy) or self.data[cx][cy] != 3 - player:
            return False
        while self.in_range(cx, cy) and self.data[cx][cy] == 3 - player:
            cx += i
            cy += j
        return self.in_range(cx, cy) and self.data[cx][cy] == player

    def flip_in_direction(self, player, x, y, i, j):
        cx, cy = x + i, y + j
        while self.in_range(cx, cy) and self.data[cx][cy] == 3 - player:
            self.data[cx][cy] = player
            cx += i
            cy += j

    def can_go_at(self, player, x, y):
        if (x, y) == (2, 3):
            pass
        if not self.in_range(x, y) or self.data[x][y] > 0:
            return False
        for i, j in self.directions:
            if self.can_flip_in_direction(player, x, y, i, j):
                return True
        return False

    def can_go(self, player):
        for i in range(8):
            for j in range(8):
                if self.can_go_at(player, i, j):
                    return True
        return False

    def go(self, pos, player):
        x, y = pos
        if not self.can_go_at(player, x, y):
            return False
        self.data[x][y] = player
        for i, j in self.directions:
            if self.can_flip_in_direction(player, x, y, i, j):
                self.flip_in_direction(player, x, y, i, j)
        return True

    def count_stone(self, player):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if self.data[i][j] == player:
                    cnt += 1
        return cnt


class Judge:
    def __init__(self, p1, p2):
        self.p1 = p1()
        self.p2 = p2()

    def run_once(self, who_first):
        if who_first == 1:
            p1, p2 = self.p1, self.p2
        else:
            p1, p2 = self.p2, self.p1
        game = Game()
        p1.new_game(1, game)
        p2.new_game(2, game)
        step = 0
        win = 0
        print('Game begins, black=%s, white=%s' % (p1.name, p2.name))
        while game.can_go(1) or game.can_go(2):
            if game.can_go(1):
                step += 1
                pos = p1.go()
                ret = game.go(pos, 1)
                print('Black(%s) goes at (%s,%s)' % (p1.name, pos[0], pos[1]))
                if not ret:
                    print('Invalid position!')
                    win = 2
                    break
                game.show()
            if game.can_go(2):
                step += 1
                pos = p2.go()
                ret = game.go(pos, 2)
                print('White(%s) goes at (%s,%s)' % (p2.name, pos[0], pos[1]))
                if not ret:
                    print('Invalid position!')
                    win = 1
                    break
                game.show()
        if win == 0:
            c1 = game.count_stone(1)
            c2 = game.count_stone(2)
            if c1 > c2:
                win = 1
                print('Black(%s) wins!' % p1.name)
            elif c1 < c2:
                win = 2
                print('White(%s) wins!' % p2.name)
        if win == 0:
            print('Draw!')
            return 0
        elif who_first == 1:
            return win
        else:
            return 3 - win


judge = Judge(Player1, Player2)
judge.run_once(1)
