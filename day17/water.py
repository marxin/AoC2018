#!/usr/bin/env python3

import re
from PIL import Image, ImageDraw
from collections import deque

points = set()
water = set()

class Stream:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 1

    def step(self):
        fall = (self.x, self.y + self.height + 1)
        if fall in points or fall in water:
            pass
        else:
            self.height += 1

streams = [Stream(500, 0)]

for line in open('input.txt').readlines():
    line = line.strip()
    m = re.match('y=(.*), x=(.*)\.\.(.*)', line)
    if m:
        y = int(m.group(1))
        x1 = int(m.group(2))
        x2 = int(m.group(3))
        for x in range(x1, x2 + 1):
            points.add((x, y))
        continue
    m = re.match('x=(.*), y=(.*)\.\.(.*)', line)
    x = int(m.group(1))
    y1 = int(m.group(2))
    y2 = int(m.group(3))
    for y in range(y1, y2 + 1):
        points.add((x, y))

width = 1000
height = 0

for p in points:
    if p[1] > height:
        height = p[1]

def draw():
    height = 300
    im = Image.new('RGB', (width, height + 10), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    for p in points:
        draw.point(p, fill = (0, 0, 0))
    for w in water:
        draw.point(w, fill = (0, 0, 256))
    for stream in streams:
        for y in range(stream.height + 1):
            draw.point((stream.x, stream.y + y), fill = (0, 256, 256))

    im.save('water.png')

for i in range(100):
    for stream in streams:
        stream.step()

"""
while tips:
    tip = tips.popleft()
    fall = (tip[0], tip[1] + 1)
    if fall in points or fall in water:
        if tip in sprinkle:
            # fill level up
            water.add(tip)
            x = 1
            overflow = False
            while True:
                p = (tip[0] + x, tip[1])
                if p in points:
                    break
                pdown = (p[0], p[1] + 1)
                if pdown in points or pdown in water:
                    water.add(p)
                else:
                    tips.append(p)
                    sprinkle.add(p)
                    overflow = True
                    break
                x += 1
            x = -1
            while True:
                p = (tip[0] + x, tip[1])
                if p in points:
                    break
                pdown = (p[0], p[1] + 1)
                if pdown in points or pdown in water:
                    water.add(p)
                else:
                    tips.append(p)
                    sprinkle.add(p)
                    overflow = True
                    break
                x -= 1
            if not overflow:
                upper = (tip[0], tip[1] - 1)
                if upper in sprinkle:
                    tips.append(upper)
    else:
        sprinkle.add(fall)
        tips.append(fall)
"""

draw()
