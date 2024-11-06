import random
import pprint


supplies = ['pens', 'staplers', "flamethrowers", 'binders']
for index,value in enumerate(supplies):
    print(f"{value} has the {index} index")
print(supplies.index("pens"))
print(random.choice(supplies))
random.shuffle(supplies)
print(supplies)

text = "hello"
text += " world !"

print(text)

# list variable is a reference to the list in memory
import copy
spam = [ "A", "B", "C"]

print(id(spam))
egg=spam
print(id(egg))

cheese = copy.copy(spam)
print(id(cheese))

dictio = {'a':1, 'B':2, 'c':3, "d":4, 'e':cheese}
print(pprint.pformat(object=dictio, indent=12))