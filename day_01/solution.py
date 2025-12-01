#!/bin/python3

import sys
from typing import List

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # lines.append(list(line))
            lines.append(line)

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    dial = 50
    for line in lines:
        dir = line[0]
        val = int(line[1:])

        if dir == "R":
            dial += val
            dial %= 100
        else:
            dial -= val
            dial %= 100

        if dial == 0:
            answer += 1

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    dial = 50
    for line in lines:
        dir = line[0]
        val = int(line[1:])

        if dir == "R":
            for i in range(0, val):
                dial += 1
                dial %= 100
                if dial == 0:
                    answer += 1
        else:
            for i in range(0, val):
                dial -= 1
                dial %= 100
                if dial == 0:
                    answer += 1

    print(f"Part 2: {answer}")


part_one()
part_two()
