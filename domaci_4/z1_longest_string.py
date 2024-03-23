from functools import reduce

strings = ["flower", "flow", "flight"]


def longest_string(lst):
    return reduce(lambda x, y: x if len(x) > len(y) else y, lst)


result = longest_string(strings)
print("Longest string:", result)
