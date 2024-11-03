# Break statements once reached exits the loop (while or for)
# Continue gets back to loop evaluation line


# WHILE LOOP WITH BREAK
# while True:
#     print('please type your name')
#     name = input()
#     if name == "your name":
#         break
# print('thanks')


# WHILE LOOP WITH CONTINUE
# while True:
#     print("who are you")
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello Joe, enter password ')
#     password = input()
#     if password == 'swordfish':
#         break
# print("access granted")


# BREAK AND CONTINUE IN FOR LOOP
# for value in range(1,5):
#     print(value)
#     if value == 4:
#         break
#     elif value == 3:
#         continue
#     print("end of loop")

# print("end of program")


# USING RANGE
# total = 0
# for number in range (101):
#     print(number)
#     total = total + number
# print(total)

import random
for i in range(5):
    print(random.randint(1,100))