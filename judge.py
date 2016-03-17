from player1 import player as player1

class chess:
    def __init__(self):
        self.data=[[(0,0) for i in range(8)] for i in range(8)]
        self.data[4][3]=(1,0)
        self.data[3][4]=(1,0)
        self.data[3][3]=(2,0)
        self.data[4][4]=(2,0)

    def stone_to_char(self,stone):
        return {0:'  ',1:'● ',2:'○ '}[stone]

    def show(self):
        print('■ '*10)
        for i in range(8):
            print('■ ',end='')
            for j in range(8):
                print(self.stone_to_char(self.data[i][j][0]),end='')
            print('■ ')
        print('■ '*10)


class judge:
    def __init__(self,p1,p2):
        self.p1=p1(self)
        self.p2=p2(self)

    def run_once(self,who_first):
        self.p1.new_game(who_first)
        self.p2.new_game(3-who_first)
        self.chess=chess()
        self.chess.show()


j=judge(player1,player1)
j.run_once(1)
