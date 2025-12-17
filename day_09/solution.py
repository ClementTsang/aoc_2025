#!/bin/python3

import sys
from typing import List
import itertools
import shapely

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[int]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # lines.append(list(line)) # Change the return to Line[Line[str]]
            lines.append(
                [int(v) for v in line.split(",")]
            )  # Change the signature to List[int]

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    for a, b in itertools.combinations(lines, 2):
        candidate = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
        if answer < candidate:
            answer = candidate

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    red_green = shapely.Polygon([(x, y) for (y, x) in lines])

    for a, b in itertools.combinations(lines, 2):
        ax = a[1]
        ay = a[0]
        bx = b[1]
        by = b[0]

        left = ax if ax < bx else bx
        right = ax if ax > bx else bx
        top = ay if ay < by else by
        bottom = ay if ay > by else by

        candidate = shapely.box(left, top, right, bottom)

        if not shapely.contains(red_green, candidate):
            continue

        area = (right - left + 1) * (bottom - top + 1)
        if answer < area:
            answer = area

    print(f"Part 2: {answer}")


part_one()
part_two()
