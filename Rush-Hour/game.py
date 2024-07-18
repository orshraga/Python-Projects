from board import Board
from helper import load_json

class Game:
    """
    Add class description here
    """
    def __init__(self):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board_game = Board()
        self.cars = list()
        self.set_game()

    def set_game(self):
        """
               Note
            - this function get a dict from json file and the DATA about each cars there is in there game
            - the function show to the user all the cars in the game
            - the function set the board game with all the car and the configure from the json file and in the end show it to the user
        """
        self.car_config = load_json("car_config.json")
        for key in self.car_config:
            self.cars.append(key)
        print(f"The available car keys in the game:\n{self.cars}\n")
        self.board_game.initial_game(self.car_config)
        self.board_game.print_board()


    def single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass


    def play(self, car, direction):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(f'move {car} to {direction}')
        if car not in self.cars:
            # raise ValueError(f"Value '{car}' not found in the list.")
            print(f"Value '{car}' not found in the car list.")
            exit()
        direction_list = ['r', 'l', 'u', 'd']
        if direction not in direction_list:
            # raise ValueError(f"Value '{direction}' not found in the list.")
            print(f"Value '{car}' not found in the direction list.")
            exit()
        car_key = f'{car}'
        self.car_turn = self.car_config[car_key]
        self.board_game.locate_car(car_key, direction)
        self.board_game.print_board()
        self.board_game.check_victory(car_key, direction)


if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    pass
