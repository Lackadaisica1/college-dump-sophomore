""" File: proj05_short.py
    Author: Abraham Aruguete
    Purpose: dude i herd you liked lists so i put a list inside yo list inside another list"""

from list_node import *

def list_to_array(head):
    """ This function does the admirable task of converting a linked list into
an array. """
    linkedArray = []
    if head == None:
        return linkedArray
    curr = head
    while curr is not None:
        linkedArray.append(curr.val)
        curr = curr.next

    return linkedArray

def array_to_list(array):
    """ This function is the inverse of list_to_array."""
    if array == []:
        noneNode = ListNode(None)
        return noneNode
 
    nodeHead = ListNode(array[0])
    curr = nodeHead
    counter = 1
    while counter < len(array):
        curr.next = ListNode(array[counter])
        curr = curr.next
        counter += 1
        

    return nodeHead


def append_list_to_list(list1, list2):
    """This function appends a linked list to another list."""
    if (list1.val == None) and (list2 == None):
        return ListNode(None)

    curr = list1
    while curr.next is not None:
        curr = curr.next

    curr.next = list2
    
    return list1

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

def split_list(head):
    """ This function takes a linked list, and splits the list into two at the middle. """
    if head.val == None:
        return ListNode(None)

    bigArray = list_to_array(head)
    if (len(bigArray)%2 == 0):
        listOne = bigArray[0:len(bigArray)//2]
        listTwo = bigArray[len(bigArray)//2:len(bigArray)]
        linkedListOne = array_to_list(listOne)
        linkedListTwo = array_to_list(listTwo)

        return linkedListOne, linkedListTwo
    
    elif(len(bigArray)%2 == 1):
        listOne = bigArray[0:len(bigArray)//2 + 1]
        listTwo = bigArray[len(bigArray)//2 + 1: len(bigArray)]
        linkedListOne = array_to_list(listOne)
        linkedListTwo = array_to_list(listTwo)

        return linkedListOne, linkedListTwo


def accordion(old_head):
    """ This function removes nodes in a given linked list in a manner described in
the project prompt. """



def too_many_aliases():
    """ This function prints out the shape in the prompt. """
    ListNode1 = ListNode(11)
    ListNode2 = ListNode(22)
    ListNode3 = ListNode(33)
    ListNode4 = ListNode(44)
    ListNode5 = ListNode([ListNode1, ListNode2])
    ListNode6 = ListNode([ListNode2, ListNode1])
    ListNode7 = [ListNode5, ListNode6, ListNode5, ListNode6]
    return ListNode7
