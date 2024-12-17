from aoc.utilities.fetch import get_input

FIRST_PATTERN = "XMAS"

def part1(data):

    n, m = len(data), len(data[0])
    ans = 0

    def check(i, j, data):
        delta_positions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, 1),   # right
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
        ]

        
        return sum(map(lambda x: check_logic(data, i, j, x[0], x[1], 0), delta_positions))

    def check_logic(data, i, j, di, dj, level):

        if not (0 <= i < len(data) and 0 <= j < len(data[0])):
            return 0
        
        if data[i][j] != FIRST_PATTERN[level]:
            return 0
        
        if level == 3:
            return 1
    
        return check_logic(data, i + di, j + dj, di, dj, level + 1)
    
    for i in range(n):
        for j in range(m):
            ans += check(i, j, data)


    return ans

data = list(map(list, get_input(4).splitlines()))

print(f"Part 1 Solution: {part1(data)}")