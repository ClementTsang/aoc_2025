#!/bin/python3

import os
import sys

import requests

# Script to pull the input for a given day. Run this with `./pull.py <DAY>`.
#
# This script caches results and prevents further pulling if
# the input was previously successfully pulled, and includes
# some user agent stuff if contact is needed.
#
# If any issues arise, please let me know!
# - Clement

day = str(int(sys.argv[1]))
print(f"Fetching input for day {day}...")

with open(f"day_{day.zfill(2)}/input.txt", "a+") as i:
    i.seek(0)
    curr = i.read()
    if len(curr) > 0 and not curr.startswith("Please don't"):
        print("Not pulling as input file is populated.")
        exit(0)

    session = os.environ["AOC_SESSION"]

    headers = {
        "Cookie": f"session={session}",
        "User-Agent": "github.com/ClementTsang/aoc_2025/blob/main/pull.py",
    }
    response = requests.get(
        f"https://adventofcode.com/2025/day/{day}/input", headers=headers
    )

    input = response.text

    print(f"Writing to day_{day.zfill(2)}/input.txt")
    i.write(input)
