# One of the self-check exercises from Problem Solving with Data Structures and
# Algorithms, Second Edition. Prompt is to:
# 1) Start time
# 2) Generate a random string
# 3) Match this with the phrase "methinks it is a weasel", if not equal
# then repeat step 2
# 4) End the time, print difference
# NOTE: THIS ONE IS EDITED FOR A "HILL CLIMBING ALGORITHM"

import time
import random


# Function which generates string randomly, and then returns False when done
# Also, uses "hill climbing" algorithim
def generate_string():
    list_of_roman_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", \
                              "i", "j", "k", "l", "m", "n", "o", "p", \
                              "q", "r", "s", "t", "u", "v", "w", "x", \
                              "y", "z", " "]

    
    true_string = "methinks it is a weasel"
    test_string = ""

    # initializing an index for the key string
    j = 0
    
    for i in range(len(true_string)):
        char = random.choice(list_of_roman_alphabet)
        while char != true_string[j]:
            char = random.choice(list_of_roman_alphabet)
        test_string += char
        j += 1
    
    return test_string    
        



def main():
    start = time.time()
    string = generate_string()

    end = time.time()
    
    print(string)
    print("Time passed: " + str(end-start))

main()
