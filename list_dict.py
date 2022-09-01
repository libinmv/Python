import itertools

inp = [{'a': 5, 'b': 2, 'e': 7}, {'c': 6, 'd': 4}]
keys = list(inp[0].keys())

counter = itertools.count(1)

keys = [list(x.keys()) for x in inp]
vals = [list(x.values()) for x in inp]
sum = [sum(x) for x in vals]
test = [print("Sum of elements in dict " + str(next(counter)) + " = " + str(i))
        for i in sum]
