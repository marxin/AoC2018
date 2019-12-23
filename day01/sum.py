#!/usr/bin/env python3

s = 0
for i in open('input.txt').readlines():
    s += int(i)

print(s)
