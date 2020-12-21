# Fix exepnse report for the Elves in accounting

# Import libraries
import numpy as np
import os
import time

# Read puzzle input
def read_puzzle_input(myfilename):
    list_of_expense_report = []
    with open(myfilename) as myfile:
        for current_row in myfile:
            list_of_expense_report.append(int(current_row))
    return list_of_expense_report

def resolve_first_half(list_of_expense_report):
    found_it = False
    entry_1 = 0
    entry_2 = 0
    for primary_element in list_of_expense_report:
        for secondary_element in list_of_expense_report:
            mysum = primary_element + secondary_element
            if mysum == 2020:
                entry_1 = primary_element
                entry_2 = secondary_element
                found_it = True
                print(f"Found it!! {entry_1}+{entry_2} = {mysum}")
                break
        if found_it:
            break
    answer = entry_1*entry_2
    return answer

def resolve_second_half(list_of_expense_report):
    found_it = False
    entry_1 = 0
    entry_2 = 0
    entry_3 = 0
    for primary_element in list_of_expense_report:
        for secondary_element in list_of_expense_report:
            for third_element in list_of_expense_report:
                mysum = primary_element + secondary_element + third_element
                if mysum == 2020:
                    entry_1 = primary_element
                    entry_2 = secondary_element
                    entry_3 = third_element
                    found_it = True
                    print(f"Found it!! {entry_1}+{entry_2}+{entry_3} = {mysum}")
                    break
            if found_it:
                break
    answer = entry_1*entry_2*entry_3
    return answer

def resolve_puzzle():
    filename = "puzzle.input"
    list_of_expense_report = read_puzzle_input( filename )
#print(list_of_expense_report)
    nb_of_lines = len(list_of_expense_report)
    print(f"Number of elements = {nb_of_lines}")
    start = time.time()
    answer = resolve_first_half(list_of_expense_report)
    print(f"The answer to the 1st half is {answer}")
    end1 = time.time() - start
    answer = resolve_second_half(list_of_expense_report)
    print(f"The answer to the 2nd half is {answer}")


resolve_puzzle()
