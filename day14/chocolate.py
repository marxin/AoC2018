#!/usr/bin/env python3

recipes = [3, 7]

a = 0
b = 1

steps = 330121
chunk = 10

while True:
    if len(recipes) > (steps + chunk):
        break
    s = recipes[a] + recipes[b]
    if s >= 10:
        n1 = s % 10
        n0 = int(s / 10)
        recipes.append(n0)
        recipes.append(n1)
    else:
        recipes.append(s)
    a = (a + recipes[a] + 1) % len(recipes)
    b = (b + recipes[b] + 1) % len(recipes)

print(''.join([str(x) for x in recipes[steps:][:10]]))
