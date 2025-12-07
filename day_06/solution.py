#!/bin/python3

import sys
from typing import List

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip("\n")
            # lines.append(list(line)) # Change the return to Line[Line[str]]
            # lines.append([int(v) for v in list(line)])) # Change the signature to List[int]
            lines.append(line)

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    values: List[List[int]] = []
    operations = []

    for line in lines:
        s = line.split()
        if s[0].isdigit():
            for i in range(len(s)):
                if len(values) < i + 1:
                    values.append([s[i]])
                else:
                    values[i].append(s[i])
        else:
            operations = s

    for vs, op in zip(values, operations):
        result = 0

        if op == "*":
            result = 1
            for v in vs:
                result *= int(v)
        else:
            for v in vs:
                result += int(v)

        answer += result

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    problems: List[List[int]] = []
    operations = []

    # Alright I'm manually parsing it. First let's scrape the operations.
    operations = lines[-1].split()

    digit_lines = lines[:-1]

    line_length = max(len(l) for l in digit_lines)

    problem = []
    for i in range(line_length):
        value = 0

        all_spaces = True
        for line in digit_lines:
            if line[i].isdigit():
                value *= 10
                value += int(line[i])
                all_spaces = False

        if all_spaces:
            problems.append(problem)
            problem = []
        else:
            problem.append(value)
            value = 0

    problems.append(problem)

    for vs, op in zip(problems, operations):
        result = 0

        if op == "*":
            result = 1
            for v in vs:
                result *= int(v)
        else:
            for v in vs:
                result += int(v)

        answer += result

    print(f"Part 2: {answer}")


part_one()
part_two()
