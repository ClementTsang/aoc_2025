#!/bin/python3

import sys
from typing import List


sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[List[str]]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


ROLL = "@"


def is_removable(lines, i, j) -> bool:
    rolls = 0
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if k == 0 and l == 0:
                continue

            if i + k >= len(lines) or j + l >= len(lines[i]) or i + k < 0 or j + l < 0:
                continue

            if lines[i + k][j + l] == ROLL:
                rolls += 1

    return rolls < 4


def part_one():
    lines = read_lines_to_list()
    answer = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ROLL:
                continue

            if is_removable(lines, i, j):
                answer += 1

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    removable = set()
    unremovable = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ROLL:
                continue

            if is_removable(lines, i, j):
                removable.add((i, j))
            else:
                unremovable.add((i, j))

    while True:
        removed = 0

        while len(removable) > 0:
            removed += 1
            to_remove = removable.pop()
            lines[to_remove[0]][to_remove[1]] = "."

            answer += 1

        if removed == 0:
            break

        for curr in unremovable:
            if is_removable(lines, curr[0], curr[1]):
                removable.add(curr)

        for r in removable:
            unremovable.remove(r)

    print(f"Part 2: {answer}")


part_one()
part_two()
