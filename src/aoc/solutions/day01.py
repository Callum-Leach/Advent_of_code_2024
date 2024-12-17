from aoc.utilities.fetch import get_input
from collections import Counter

def split(input):
    first, second = [], []
    for line in input.splitlines():
        a, b = map(int, line.split())
        first.append(a)
        second.append(b)

    return first, second

def part1(first, second):
    ans = 0
    for a, b in zip(sorted(first), sorted(second)):
        ans += abs(a - b)
    
    return ans

def part2(first, second):
    c = Counter(second)

    ans = 0
    for e in first:
        ans += e * c.get(e, 0)
    
    return ans

first, second = split(get_input(1))

print(f"Part 1 Solution: {part1(first, second)}")
print(f"Part 2 Solution: {part2(first, second)}")