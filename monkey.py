# One of the self-check exercises from Problem Solving with Data Structures and
# Algorithms, Second Edition. Prompt is to:
# 1) Start time
# 2) Generate a random string
# 3) Match this with the phrase "methinks it is a weasel", if not equal
# then repeat step 2
# 4) End the time, print difference

import time
import random


# Function which generates random string 
def generate_string():
    list_of_roman_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", \
                              "i", "j", "k", "l", "m", "n", "o", "p", \
                              "q", "r", "s", "t", "u", "v", "w", "x", \
                              "y", "z", " "]
    
    test_string = ""
    for i in range(27):
        char = random.choice(list_of_roman_alphabet)
        test_string += char
    return test_string


def check_string(string):
    if string == "methinks it is a weasel":
        return False
    else:
        return True


def main():
    start = time.time()

    string = generate_string()

    while check_string(string):
        string = generate_string()

    end = time.time()

    print("Time passed: " + str(end-start))

main()
    
        
