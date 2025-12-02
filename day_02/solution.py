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


def invalid_id(s):
    if len(s) % 2 != 0:
        return False
    half = int(len(s) / 2)

    return s[:half] == s[half:]


def part_one():
    lines = read_lines_to_list()
    answer = 0

    ranges = lines[0].split(",")
    for r in ranges:
        if "-" not in r:
            continue
        rs = r.split("-")

        start = int(rs[0])
        end = int(rs[1])

        for curr in range(start, end + 1):
            c = str(curr)
            if invalid_id(c):
                answer += curr

    print(f"Part 1: {answer}")


def invalid_id_2(s):
    for i in range(0, len(s) // 2 + 1):
        curr = s[0:i]

        # Just brute force 10 checks... what's the worst that can happen?
        for n in range(1, 10):
            if curr * n == s[i:]:
                return True
    return False


def part_two():
    lines = read_lines_to_list()
    answer = 0

    ranges = lines[0].split(",")
    for r in ranges:
        if "-" not in r:
            continue
        rs = r.split("-")

        start = int(rs[0])
        end = int(rs[1])

        for curr in range(start, end + 1):
            c = str(curr)
            if invalid_id_2(c):
                answer += curr

    print(f"Part 2: {answer}")


part_one()
part_two()
