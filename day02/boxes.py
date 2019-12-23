#!/usr/bin/env python3

def has_arity(text, n):
    d = {}
    for s in text:
        if not s in d:
            d[s] = 1
        else:
            d[s] += 1
    for k, v in d.items():
        if v == n:
            return True
    return False

boxes = [l.strip() for l in open('input.txt').readlines()]

two = sum([int(has_arity(x, 2)) for x in boxes])
three = sum([int(has_arity(x, 3)) for x in boxes])

print(two)
print(three)
print(two * three)
