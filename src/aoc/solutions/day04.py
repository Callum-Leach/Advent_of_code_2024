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

def part1_2(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word = "XMAS"
    word_length = len(word)
    
    # All eight directions
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, 1),   # right
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
    ]
    
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            # If the starting letter matches 'X', only then proceed
            if grid[r][c] == 'X':
                for dx, dy in directions:
                    # Check if we can find "XMAS" in this direction
                    rr, cc = r, c
                    matched = True
                    for i in range(1, word_length):
                        rr += dx
                        cc += dy
                        if not in_bounds(rr, cc) or grid[rr][cc] != word[i]:
                            matched = False
                            break
                    if matched:
                        count += 1
    return count

data = list(map(list, get_input(4).splitlines()))
print(f"Part 1 Solution: {count_xmas_occurrences(data)}")