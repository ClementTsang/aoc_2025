#!/bin/python3

import sys
from typing import List


sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[int]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append([int(v) for v in list(line)])

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    for bank in lines:
        best = 0
        for i in range(0, len(bank)):
            first = bank[i]
            for j in range(i + 1, len(bank)):

                curr = first * 10 + bank[j]
                if curr > best:
                    best = curr

        answer += best

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    for bank in lines:
        best = 0
        best_str = ""

        for i in range(12):
            best *= 10
            best += bank[i]

        best_str = str(best)

        prev = 12

        while prev < len(bank):
            curr_digit = bank[prev]
            for j in range(0, len(best_str)):
                curr = best_str[:j] + best_str[j + 1 :] + str(curr_digit)
                curr_int = int(curr)

                if curr_int > best:
                    best = curr_int
                    best_str = curr
                    break

            prev += 1

        answer += best

    print(f"Part 2: {answer}")


part_one()
part_two()
