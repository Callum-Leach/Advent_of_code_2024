from aoc.utilities.fetch import get_input
from collections import Counter 

def part1(input):
    return Counter(map(check, input)).get(True, 0)

def part2(input):
    def force_check(line):
        n = len(line)
        candidates = [list(line) for _ in range(n)]

        for can, i in zip(candidates, range(n)):
            can.pop(i)

        return any(map(check, candidates))
    
    return Counter(map(force_check, input)).get(True, 0)



def check(line):
    def f(line):
        for i in range(1, len(line)):
            # Check whether two adjacent number differ by at least one and at most three.
            if not (1 <= (line[i] - line[i-1]) <= 3):
                return False
        return True
    
    def g(line):
        for i in range(1, len(line)):
            if not (1 <= (line[i-1] - line[i]) <= 3):
                return False
        return True
    
    return f(line) or g(line)




data = [list(map(int, line.split())) for line in get_input(2).splitlines()]

print(f"Part 1 Solution: {part1(data)}")
print(f"Part 2 Solution: {part2(data)}")
