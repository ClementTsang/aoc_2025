#!/bin/python3

import sys
from typing import List
import functools

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # lines.append(list(line)) # Change the return to Line[Line[str]]
            # lines.append([int(v) for v in line])  # Change the signature to List[int]
            lines.append(line)

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    connections = {}

    for line in lines:
        [device, rest] = line.split(":")
        outputs = rest.strip().split()

        connections[device] = outputs

    queue = [("you", ["you"])]

    while len(queue) > 0:
        (curr, path) = queue.pop(0)

        if curr == "out":
            # print(path)
            answer += 1

        if curr not in connections:
            continue

        children = connections[curr]
        for child in children:
            new_path = path.copy()
            new_path.append(child)
            queue.append((child, new_path))

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    connections = {}

    for line in lines:
        [device, rest] = line.split(":")
        outputs = rest.strip().split()

        connections[device] = outputs

    @functools.cache
    def dfs(curr: str, has_fft: bool, has_dac: bool):
        if curr == "out":
            if has_dac and has_fft:
                return 1
            else:
                return 0

        if curr not in connections:
            return 0

        children = connections[curr]

        out = 0
        for child in children:
            if child == "fft":
                out += dfs(child, True, has_dac)
            elif child == "dac":
                out += dfs(child, has_fft, True)
            else:
                out += dfs(child, has_fft, has_dac)

        return out

    answer = dfs("svr", False, False)

    print(f"Part 2: {answer}")


part_one()
part_two()
