""" File: prob1.py
    Author: Abraham Aruguete
    Purpose: i think this is a review of classes or something"""


class Simplest:
    """ This is a simple class for simple folk."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    """This is a class which has three parameters, getter and setter methods, and a rotate method which shifts the three parameters. """

    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

    def get_third(self):
        return self._third
    
    def rotate(self):
        tempVar = self._first
        self._first = self._second
        self._second = self._third
        self._third = tempVar


class Band:
    """ This class is a class which represents a musical group. It starts out with one singer, a None drummer, and zero guitar players, and has various attributes which modify these things. """


    def __init__(self, singer):
        self._singer = singer
        self._drummer = None
        self._guitar_players = 0
        self._guitar_players_list = []
    
    def get_singer(self):
        return self._singer

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_drummer(self):
        return self._drummer

    def set_drummer(self, new_drummer):
        self._drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self._guitar_players += 1
        self._guitar_players_list.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self._guitar_players = 0
        self._guitar_players_list = []

    def get_guitar_players(self):
        newList = self._guitar_players_list
        return newList

    def play_music(self):
        if (self._singer == "Frank Sinatra"):
            print("Do be do be do")
        elif (self._singer == "Kurt Cobain"):
            print("bargle nawdle zouss")
        else:
            print("La la la")
        if (self._drummer != None):
            print("Bang bang bang!")
        for index in range(self._guitar_players):
            print("Strum!")


        
