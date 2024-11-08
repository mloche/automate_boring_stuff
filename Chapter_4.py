import random
import pprint


# supplies = ['pens', 'staplers', "flamethrowers", 'binders']
# for index,value in enumerate(supplies):
#     print(f"{value} has the {index} index")
# print(supplies.index("pens"))
# print(random.choice(supplies))
# random.shuffle(supplies)
# print(supplies)

# text = "hello"
# text += " world !"

# print(text)

# # list variable is a reference to the list in memory
# import copy
# spam = [ "A", "B", "C"]

# print(id(spam))
# egg=spam
# print(id(egg))

# cheese = copy.copy(spam)
# print(id(cheese))

# dictio = {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2,
# 'i': 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1, 'z':[ "A", "B", "C"]}
# print(pprint.pformat(object=dictio, indent=2))
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)