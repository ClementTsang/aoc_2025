#!/bin/python3

import sys
from copy import deepcopy
from heapq import heappop, heappush
from typing import List, Tuple

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # lines.append(list(line)) # Change the return to Line[Line[str]]
            # lines.append([int(v) for v in list(line)])) # Change the signature to List[int]
            lines.append(line)

    return lines


def get_start(maze: List[List[str]]) -> Tuple[int, int]:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return (i, j)


def get_splitters(maze: List[List[str]]) -> List[Tuple[int, int]]:
    out = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "^":
                out.append((i, j))

    return out


def part_one():
    maze = read_lines_to_list()
    answer = 0

    start = get_start(maze)
    splitters = set(get_splitters(maze))

    beams = [(start[0] + 1, start[1])]
    splits = set()
    visited = set()

    while len(beams) > 0:
        beam = beams.pop()

        if beam in visited:
            continue

        visited.add(beam)

        if beam in splitters:
            splits.add(beam)
            if beam[1] - 1 >= 0:
                beams.append((beam[0], beam[1] - 1))

            if beam[1] + 1 < len(maze[0]):
                beams.append((beam[0], beam[1] + 1))
        else:
            new_beam = (beam[0] + 1, beam[1])
            if new_beam[0] < len(maze):
                beams.append(new_beam)

    answer = len(splits)
    print(f"Part 1: {answer}")


def part_two():
    maze = read_lines_to_list()
    answer = 0

    start = get_start(maze)
    splitters = set(get_splitters(maze))

    from functools import cache

    @cache
    def timelines(beam):
        if beam in splitters:
            a = 0
            b = 0

            if beam[1] - 1 >= 0:
                new_beam = (beam[0], beam[1] - 1)

                a = timelines(new_beam)

            if beam[1] + 1 < len(maze[0]):
                new_beam = (beam[0], beam[1] + 1)

                b = timelines(new_beam)

            return a + b
        else:
            new_beam = (beam[0] + 1, beam[1])
            if new_beam[0] < len(maze):
                return timelines(new_beam)
            else:
                return 1

    answer = timelines(start)
    print(f"Part 2: {answer}")


part_one()
part_two()
