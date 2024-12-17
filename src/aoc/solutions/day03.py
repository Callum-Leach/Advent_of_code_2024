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

def part2(data):

    pattern = r"(mul|do|don\'t)\((\d+,\d+|)\)"

    ans = 0
    enabled = True

    for match in re.findall(pattern, data):
        op, args = match

        if op != "mul":
            enabled = op == "do"
            continue
        
        a, b = args.split(",")
        if not enabled or not ((1 <= len(a) <= 3) and (1 <= len(b) <= 3)):
            continue

        ans += int(a) * int(b)

    return ans

def part2_2(data):
    pattern = r"(do\(\)|don't\(\)|mul\(\s*(\d+)\s*,\s*(\d+)\s*\))"

    mul_enabled = True
    ans = 0

    # Find all occurrences of do(), don't(), or mul(...) instructions
    instructions = re.findall(pattern, data)

    for instr in instructions:
        full_match = instr[0]  # The entire matched instruction
        a_str = instr[1]
        b_str = instr[2]

        if full_match == "do()":
            mul_enabled = True
        elif full_match == "don't()":
            mul_enabled = False
        elif full_match.startswith("mul("):
            if mul_enabled:
                if (1 <= len(a_str) <= 3) and (1 <= len(b_str) <= 3):
                    ans += int(a_str) * int(b_str)

    return ans

data = get_input(3)

print(f"Part 1 Solution: {part1(data)}")
print(f"Part 2 Solution: {part2(data)}")