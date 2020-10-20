""" File: prob3.py
    Author: Abraham Aruguete
    Purpose: i think this is a review of classes or something"""


class Room:
    """ This is a class which represents a room. It looks suspiciously like a linked list, but with four doors. """

    def __init__(self, name, n, s, e, w):
        self._name = name
        self.n = n
        self.s = s
        self.e = e
        self.w = w


    def get_name(self):
        return self._name

    
    def set_name(self, name):
        self._name = name

    def collapse_room(self):
        if self.e != None:
            self.e.w = None
            self.e = None
        if self.w != None:
            self.w.e = None
            self.w = None
        if self.n != None:
            self.n.s = None
            self.n = None
        if self.s != None:
            self.s.n = None
            self.s = None


def build_grid(wid, hei):
    gridObject = Room("grid", None, None, None, None)
    curr1 = gridObject
    for index1 in range(0, hei):
        curr1.n = Room(str(index1), None, curr1, None, None)
        curr2 = curr1
        for index2 in range(0, wid):
            curr2.e = Room(str(index1) + str(index2), None, None, None, curr2)
            curr2 = curr2.e
        curr1 = curr1.n
    
            
