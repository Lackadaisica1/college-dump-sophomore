""" File: cover_list_code.py
    Author: Abraham Aruguete
    Purpose: This is a script designed to test each of the lines in list_insert.py"""

from list_insert import *


def main():
    node1 = ListNode( (-8, -7) )
    node2 = ListNode ( (2, 5) )
    node3 = ListNode ( (-9, -7))
    sorted_list_insert(None, node2)
    sorted_list_insert(node1, node2)
    sorted_list_insert(node3, node1)
    sorted_list_insert(node1, node3)
    print_list(None)
    print_list(node1)

main()
