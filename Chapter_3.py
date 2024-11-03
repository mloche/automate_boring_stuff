 # SUITE DE SYRACUSE, COLLATZ SEQUENCE

import sys


def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return(number // 2)
    else:
        print(3 * number + 1)
        return(3 * number + 1)

value = input("type a number")
try :
    int(value)
    run = True
    while run:
        if value == 1:
            sys.exit(f"We reached {value} !")
        else:
            value = collatz(int(value))
except ValueError:
    print("Value must be an integrer")
    sys.exit("Invalid value type")