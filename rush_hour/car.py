
class Car:
    """
    This class represents the cars that will be on the board
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__CarName = name
        self.__CarLength = length
        self.__CarLocation = location
        self.__CarOrient = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates = list()
        for i in range(self.__CarLength):
            if self.__CarOrient == 0:
                coordinates.append((self.__CarLocation[0], self.__CarLocation[1] + i))
            if self.__CarOrient == 1:
                coordinates.append((self.__CarLocation[0] + i, self.__CarLocation[1]))
        return coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.__CarOrient == 0 :
            return {'u': "cause the car move up",
                    'd': "cause the car move down",
        }
        if self.__CarOrient ==1:
            return {'r': "cause the car move right",
                        'l': "cause the car move up"
        }

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        coord = self.car_coordinates()
        optional_move = list()
        last_cor = coord[self.__CarLength]
        if self.__CarOrient == 0 & movekey == 'r':
            optional_move.append((last_cor[0], last_cor[1] + 1))
        if self.__CarOrient == 0 & movekey == 'l':
            optional_move.append((self.__CarLocation[0], self.__CarLocation[1] - 1))
        if self.__CarOrient == 0 & movekey == 'u':
            optional_move.append((last_cor[0] + 1, last_cor[1]))
        if self.__CarOrient == 0 & movekey == 'd':
            optional_move.append((self.__CarLocation[0] - 1, self.__CarLocation[1]))
        return optional_move

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey == 'r' & self.__CarOrient == 0:
            self.__CarLocation = (self.__CarLocation[0], self.__CarLocation[1] + 1)
            return True
        if movekey == 'r' & self.__CarOrient == 1:
            return False
        if movekey == 'l' & self.__CarOrient == 0:
            self.__CarLocation = (self.__CarLocation[0], self.__CarLocation[1] - 1)
            return True
        if movekey == 'l' & self.__CarOrient == 1:
            return False
        if movekey == 'u' & self.__CarOrient == 1:
            self.__CarLocation = (self.__CarLocation[0] - 1, self.__CarLocation[1])
            return True
        if movekey == 'u' & self.__CarOrient == 0:
            return False
        if movekey == 'd' & self.__CarOrient == 1:
            self.__CarLocation = (self.__CarLocation[0] + 1, self.__CarLocation[1])
            return True
        if movekey == 'd' & self.__CarOrient == 0:
            return False

    def get_car_name(self):
        """
        :return: The name of this car.
        """
        return self.__CarName

    def get_car_location(self):
        """
        :return: The location of this car.
        """
        return self.__CarLocation

    def get_car_length(self):
        """
        :return: The length of this car.
        """
        return self.__CarLength

    def get_car_orient(self):
        """
        :return: The orientation of this car.
        """
        return self.__CarOrient

