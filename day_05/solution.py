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
            lines.append(line)

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    read_ids = False
    ranges = []

    for line in lines:
        if line == "":
            read_ids = True
            continue

        if not read_ids:
            split = line.split("-")
            start = int(split[0])
            end = int(split[1])

            ranges.append((start, end))
        else:
            id = int(line)
            for r in ranges:
                if id >= r[0] and id <= r[1]:
                    answer += 1
                    break

    print(f"Part 1: {answer}")


def overlap(a, b) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])


def part_two():
    lines = read_lines_to_list()
    answer = 0
    ranges = []

    for line in lines:
        if line == "":
            break

        split = line.split("-")
        start = int(split[0])
        end = int(split[1])

        ranges.append((start, end))

    while True:
        curr_len = len(ranges)
        for i in range(len(ranges)):
            should_exit = False

            for j in range(len(ranges)):
                if j == i:
                    continue

                r = ranges[i]
                s = ranges[j]
                if overlap(r, s):
                    ranges[i] = (min(r[0], s[0]), max(r[1], s[1]))
                    ranges.pop(j)

                    should_exit = True
                    break

            if should_exit:
                break

        if curr_len == len(ranges):
            break

    for r in ranges:
        answer += r[1] - r[0] + 1

    print(f"Part 2: {answer}")


part_one()
part_two()
