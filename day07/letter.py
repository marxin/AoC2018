#!/usr/bin/env python3

lines = open('input.txt').readlines()

dependencies = {}

for l in lines:
    parts = l.split(' ')
    needed = parts[1]
    node = parts[-3]
    if not node in dependencies:
        dependencies[node] = set()
    dependencies[node].add(needed)
    if not needed in dependencies:
        dependencies[needed] = set()

def make_step():
    global result
    if not len(dependencies):
        return None
    candidates = [(k, v) for k, v in dependencies.items() if not len(v)]
    selected = sorted(candidates, key = lambda x: x[0])[0]
    letter = selected[0]
    for k, v in dependencies.items():
        v.discard(letter)
    del dependencies[letter]
    return letter

result = ''
while True:
    s = make_step()
    if s == None:
        print(result)
        break
    else:
        result += s
