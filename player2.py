class Player:
    name = 'Player2'

    def __init__(self):
        pass

    def new_game(self, who, game):
        self.who = who
        self.game = game

    def go(self):
        for i in range(8):
            for j in range(8):
                if self.game.can_go_at(self.who, i, j):
                    return i, j
        return 0, 0
