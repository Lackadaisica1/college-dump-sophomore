""" File: proj05_long.py
    Author: Abraham Aruguete
    Purpose: so this one is the big one"""
def list_length(head):
    """This function returns the length of a given list. If it's not empty."""
    if (head.val == None):
        return 0

    counter = 0
    curr = head
    while curr is not None:
        curr = curr.next
        counter += 1

    return counter

def is_sorted(head):
    """ This function takes in a linked list, and returns True or False if the
values in the list are sorted in ascending order. """

    sortedFlag = True
    if head is None:
        return sortedFlag
    elif list_length(head) == 1:
        return sortedFlag
    
    curr = head
    value = head.val
    while curr is not None:
        if value > curr.val:
            sortedFlag = False
        value = curr.val
        curr = curr.next
        
    return sortedFlag


def list_sum(head):
    """ This function takes in a linked list, and returns the sum of the linked
list. """

    sumOfList = 0
    if head is None:
        return sumOfList
    curr = head
    while curr is not None:
        sumOfList += curr.val
        curr = curr.next

    return sumOfList
