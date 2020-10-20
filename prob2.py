""" File: prob2.py
    Author: Abraham Aruguete
    Purpose: i think this is a review of classes or something"""


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
         print(f"#"self._r={self._r:02X}self._g={self_g:02X}self._b={self_b:02X})


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
