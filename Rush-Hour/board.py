import numpy as np
ROW_NUM = 7
COL_NUM = 7
TARGET_LOCATION = (3, 7)
class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.Matrix = [['-' for _ in range(COL_NUM)] for _ in range(ROW_NUM)]
        self.board_car_config = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
    def initial_game(self, car_config):
        self.board_car_config = car_config
        for key in self.board_car_config:
            car_key = f'{key}'
            car_values = self.board_car_config[car_key]
            car_len = car_values[0]
            car_row = car_values[1][0]
            car_col = car_values[1][1]
            car_orientetion = car_values[2]
            if (car_orientetion == 0):
                for i in range(car_len):
                    self.Matrix[car_row+i][car_col] = car_key
            else:
                for i in range(car_len):
                    self.Matrix[car_row][car_col+i] = car_key

    def debug(self, row, col):
        self.Matrix[row][col] = 'x'

    def print_board(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        for i in range(3):
            print(self.Matrix[i])
        print(self.Matrix[3], '<--')
        for i in range(4, 7, 1):
            print(self.Matrix[i])

    def locate_car(self,car_key, direction):
        car_key = f'{car_key}'
        car_values = self.board_car_config[car_key]
        car_values[1] = self.where_is_car(car_key)
        car_orientetion = car_values[2]
        car_len = car_values[0]
        car_row = car_values[1][0]
        car_col = car_values[1][1]
        """
        the following code line set values in the board game,
        the start and the end of the car becouse in one step only those twe value get change.
        the code is for four cases: 'r','l','u','d'
        """

        if(self.possible_moves(car_key, car_values, direction)):
            if (car_orientetion == 0 and direction == 'u'):
                self.Matrix[car_row -1][car_col] = car_key
                self.Matrix[car_row + car_len - 1][car_col] = '-'
            elif (car_orientetion == 0 and direction == 'd'):
                self.Matrix[car_row + car_len][car_col] = car_key
                self.Matrix[car_row][car_col] = '-'
            elif (car_orientetion == 1 and direction == 'l'):
                self.Matrix[car_row][car_col-1] = car_key
                self.Matrix[car_row][car_col + car_len-1] = '-'
            elif (car_orientetion == 1 and direction == 'r'):
                self.Matrix[car_row][car_col+car_len] = car_key
                self.Matrix[car_row][car_col] = '-'
        else:
            raise ValueError(f"can not do this move.")

    def where_is_car(self, car_key):
        for row in range(ROW_NUM):
            for col in range(COL_NUM):
                if self.Matrix[row][col] == car_key:
                    return (row, col)





    def possible_moves(self,car_key, car_values, direction):
        """
      the following code line set check if the step can be done
      thing to consider:
      when the input direction ('r','l','u','d') are fit the car.
      horizontal car = left or right, vertical car = up or down.

      the function check that the next location is empty ('-')

      the function check that the move is not outside to the board boundaries
        """

        if (car_values[2] == 0 and direction == 'u'):
            if ((self.Matrix[car_values[1][0]-1][car_values[1][1]]==('-') and (car_values[1][0]-1) >=0)):
                return True
        elif (car_values[2] == 0 and direction == 'd'):
            if ((self.Matrix[car_values[1][0]+car_values[0]][car_values[1][1]] == ('-') and (car_values[1][0]+car_values[0]) <=6)):
                return True
        elif (car_values[2] == 1 and direction == 'l'):
            if ((self.Matrix[car_values[1][0]][car_values[1][1]-1] == ('-') and (car_values[1][1]-1) >=0)):
                return True
        elif (car_values[2] == 1 and direction == 'r'):
            if ((self.Matrix[car_values[1][0]][car_values[1][1]+car_values[0]] == ('-') and (car_values[1][1]+car_values[0]) <=6)):
                return True
        return False

    def check_victory(self, car_key, direction):
        """   the following function check if the user won,
        this check is relevant only when the user move car left.
        if the user moved car left and the current car is in the gate, the user won
              """
        if (self.Matrix[3][6] == car_key and direction == 'r'):
            print("!!!! YOU WON!!!!!")
            exit()