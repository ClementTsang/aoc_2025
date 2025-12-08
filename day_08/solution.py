#!/bin/python3

import heapq
import sys
from typing import List
import math
import networkx as nx


sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
TIMES = 10 if "test.txt" in FILE else 1000


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # lines.append(list(line)) # Change the return to Line[Line[str]]
            # lines.append([int(v) for v in list(line)])) # Change the signature to List[int]
            lines.append([int(x) for x in line.split(",")])

    return lines


def distance(x1, y1, z1, x2, y2, z2) -> int:
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2))


def part_one():
    lines = read_lines_to_list()
    answer = 0

    graph = nx.Graph()
    for x, y, z in lines:
        graph.add_node((x, y, z))

    smallest = []
    seen = set()
    heapq.heapify(smallest)
    for x, y, z in lines:
        for x2, y2, z2 in lines:
            if x == x2 and y == y2 and z == z2:
                continue

            dist = distance(x, y, z, x2, y2, z2)
            heapq.heappush(smallest, (dist, (x, y, z), (x2, y2, z2)))

    for i in range(TIMES):
        while True:
            (dist, a, b) = heapq.heappop(smallest)
            if (a, b) not in seen and (b, a) not in seen:
                graph.add_edge(a, b)
                seen.add((a, b))
                seen.add((b, a))
                break

    components = sorted(
        nx.connected_components(graph), key=lambda x: len(x), reverse=True
    )
    answer = len(components[0]) * len(components[1]) * len(components[2])

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    graph = nx.Graph()
    for x, y, z in lines:
        graph.add_node((x, y, z))

    smallest = []
    seen = set()
    heapq.heapify(smallest)
    for x, y, z in lines:
        for x2, y2, z2 in lines:
            if x == x2 and y == y2 and z == z2:
                continue

            dist = distance(x, y, z, x2, y2, z2)
            heapq.heappush(smallest, (dist, (x, y, z), (x2, y2, z2)))

    while nx.number_connected_components(graph) != 1:
        while True:
            (dist, a, b) = heapq.heappop(smallest)
            if (a, b) not in seen and (b, a) not in seen:
                graph.add_edge(a, b)
                seen.add((a, b))
                seen.add((b, a))

                answer = a[0] * b[0]
                break

    print(f"Part 2: {answer}")


part_one()
part_two()
