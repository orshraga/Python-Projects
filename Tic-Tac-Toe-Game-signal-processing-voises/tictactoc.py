class tiktaktok():
    def __init__(self):
        self.reset_map()
        self.turn = 'x'
        self.num_of_turns = 0

    def play_turn(self, row, column):
        self.set_symbol(row, column)
        self.num_of_turns += 1
        self.print_map()
        if self.check_vicktory():
            print("{} ".format(self.turn) + "is the winner")
            exit(0)
        self.switch_turn()


    def switch_turn(self):
        if self.turn == 'x':
            self.turn = '0'
        elif self.turn == '0':
            self.turn = 'x'

    def set_symbol(self, row, column):
        self.check_exception(row, column)
        self.map[row][column] = self.turn

    def reset_map(self):
        self.map = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def check_vicktory(self):
        ##### check rows
        for row in self.map:
            if row[0] == row[1] == row[2] and row[0]:
                return True
        ##### check columns
        for i in range(0, 2):
            if self.map[0][i] == self.map[1][i] == self.map[2][i] and self.map[2][i]:
                return True
        ##### check diagonals
        if self.map[0][0] == self.map[1][1] == self.map[2][2] and self.map[2][2]:
            return True
        elif self.map[0][2] == self.map[1][1] == self.map[2][0] and self.map[2][0]:
            return True

    def check_exception(self, row, column):
        if (self.map[row][column] == 'x') or (self.map[row][column] == '0'):
            raise Exception("Sorry, this place is already taken")
        else:
            pass

    def print_map(self):
        for row in self.map:
            print(row)
        print('------')