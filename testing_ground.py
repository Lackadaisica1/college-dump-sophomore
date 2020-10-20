


class Simplest: #verified
    """ This is a simple class for simple folk."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Rotate: #verified
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

    def fire_all_guitar_players(self):
        self._guitar_players = 0

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


class Color:
    """ This class represents an RGB color. """

    def __init__(self, r, g, b):

        self._r = r
        self._g = g
        self._b = b

        
        if (r >= 255):
            self._r = 255
        if (g >= 255):
            self._g = 255
        if (b >= 255):
            self._b = 255
        if (r <= 0):
            self._r = 0
        if (g <= 0):
            self._g = 0
        if (b <= 0):
            self._b = 0

        


    def __str__(self):
        return "rgb({},{},{})".format(self._r, self._g, self._b)

    def html_hex_color(self):
        return f"#self._r={self._r:02X}self._g={self_g:02X}self._b={self_b:02X}"

    def get_rgb(self):
        return (self._r, self._g, self._b)

    def set_standard_color(self, name):
        assert name.upper() == "RED" or name.upper() == "YELLOW" or name.upper() == "WHITE" or name.upper() == "BLACK"
        if (name.upper() == "YELLOW"):
            self._r = 255
            self._g = 255
            self._b = 0

        elif (name.upper() == "RED"):
            self._r = 255
            self._g = 0
            self._b = 0

        elif (name.upper() == "WHITE"):
            self._r = 255
            self._g = 255
            self._b = 255

        elif (name.upper() == "BLACK"):
            self._r = 0
            self._g = 0
            self._b = 0


    
    def remove_red(self):
        self._r = 0



obj = Color(0, 500, 0)
x = str(obj)
print(x)
obj.set_standard_color("WHITE")
