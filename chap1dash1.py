#Name: Abraham Aruguete
#This is yet another block of practice code from the book "Data Structures and Algorithms in Python". This is the first chapter, Chapter 1-1.
#Woo.


#Exercise 1-1: Write a short Python function, is_multiple(n, m), that takes two integer values m and n and returns True if n is a multiple of m and False otherwise.
def is_multiple(n, m):
    if (n % m == 0):
        return True
    else:
        return False

#Exercise 1-2: Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators
def is_even(k):
    if ((k != 0 or k != 1 or k != -1) and k > 0):
        k -= 2
    elif ((k != 0 or k != 1 or k != -1) and k < 0):
        k += 2
    else:
        if k == 0:
            return True
        elif k == 1:
            return False
        else:
            return False
    #i do not endorse this code this is solely for the sake of exercises

#Exercise 1-3: Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and the largest numbers, in the form
#of a tuple of length two. Do not use the built in functions min or max in implementing your solution.
def minmax(data):
    maximum = data[0]
    minimum = data[0]
    for i in data:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    return (maximum, minimum)

#Exercise 1-4: Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers less than n
def sum_of_squares(n):
    if (n <= 0):
        return 0
    else:
        return (n*(n+1)*(2*n+1))//6

#Exercise 1-6: Write a short Python function that takes a positive integer n and returns the sum of the squares of all odd positive integers smaller than n
def sum_of_odd_squares(n):
    total_sum = 0
    for index in range(n):
        if(index%2 != 0):
            total_sum += index
    return total_sum
