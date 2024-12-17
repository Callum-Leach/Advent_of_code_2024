import re
from aoc.utilities.fetch import get_input


def part1(data):
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    ans = 0
    for mul in re.findall(pattern, data):
        a, b = mul
        if not ((1 <= len(a) <= 3) and (1 <= len(b) <= 3)):
            continue
        else:
            ans += int(a) * int(b)
    
    return ans



data = get_input(3)

print(f"Part 1 Solution: {part1(data)}")