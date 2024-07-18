class four_in_line():
    def __init__(self):
        self.reset_map()
        self.turn = 'A'
        self.num_of_players = 2
        self.row = 0

    def play_turn(self, column):
        self.set_symbol(column)
        self.print_map()
        if self.check_victory():
            print("{} ".format(self.turn) + "is the winner")
            exit(0)
        self.switch_turn()

    def reset_map(self):
        self.map = [[None, None, None, None], [None, None, None, None], [None, None, None, None],
                    [None, None, None, None], [None, None, None, None], [None, None, None, None]]

    def set_symbol(self, column):
        self.set_location(column)
        self.map[self.row][column]= self.turn

    def set_location(self, column):
        for i in range(5, -1, -1):
            if self.map[i][column] == None:
                self.row = i
                break
            else:
                pass
        if self.map[0][column]:
            raise Exception("Sorry, this place is already taken")

    def switch_turn(self):
        if self.turn == 'A':
            self.turn = 'B'
        elif self.turn == 'B':
            self.turn = 'A'

    def print_map(self):
        for row in self.map:
            print(row)
        print('------')

    def check_victory(self):
        for i in range(5, 2, -1):
            if self.map[i][0] == self.map[i][1] == self.map[i][2] == self.map[i][3] and self.map[i][3]:
                return True
        for i in range(5, 2, -1):
            if self.map[i][0] == self.map[i-1][1] == self.map[i-2][2] == self.map[i-3][3] and self.map[i-3][3]:
                return True
        for i in range(5, 2, -1):
            if self.map[i][3] == self.map[i-1][2] == self.map[i-2][1] == self.map[i-3][3] and self.map[i-3][3]:
                return True
        for j in range(0, 3):
            for i in range(5, 2, -1):
                if self.map[i][j] == self.map[i - 1][j] == self.map[i - 2][j] == self.map[i - 3][j] and self.map[i - 3][j]:
                    return True