#!/usr/bin/env python3

from termcolor import colored

N = 100
S = N / 2

input = open('input.txt').readlines()
coordinates = [tuple([int(y) + S for y in x.split(', ')]) for x in input]
colors = len(coordinates)
print(colors)

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def flood(coordinates, n):
    queue = []
    flood = {}
    for i, c in enumerate(coordinates):
        flood[c] = (i, 0)
        queue.append(c)

    inf = set()
    while len(queue):
        item = queue[0]
        f = flood[item]
        queue = queue[1:]
        for d in directions:
            newpos = (item[0] + d[0], item[1] + d[1])
            if not newpos in flood:
                steps = f[1] + 1

                conflict = False
                for d2 in directions:
                    newpos2 = (newpos[0] + d2[0], newpos[1] + d2[1])
                    if newpos2 in flood:
                        f2 = flood[newpos2]
                        if f2[0] != f[0] and f2[1] <= f[1]:
                            conflict = True
                            break

                if steps < n:
                    if not conflict:
                        flood[newpos] = (f[0], steps)
                        queue.append(newpos)
                else:
                    inf.add(f[0])

    return (flood, inf)

print(coordinates)
f, inf = flood(coordinates, 500)

"""
for i in range(N):
    for j in range(N):
        if (i, j) in f:
            t = f[(i, j)]
            c = t[0]
            if (i, j) in coordinates:
                c = colored(c, 'red')
            print(c, end = '')
        else:
            print('.', end = '')
    print()
"""

max = 0
for c in range(colors):
    if not c in inf:
        s = 0
        for k, v in f.items():
            if v[0] == c:
                s += 1
        if s > max:
            max = s

print(max)
