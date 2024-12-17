from aoc.utilities.fetch import get_input

FIRST_PATTERN = "XMAS"
SECOND_PATTERN = ["MAS", "SAM"]

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

def part2(data):
    n, m = len(data), len(data[0])
    ans = 0

    def check_second(i, j, data):
        delta_positions = [(1, 1), (-1, 1)]
        start = [(i, j), (i + 2, j)]

        for (di, dj), (si, sj) in zip(delta_positions, start):
            word = ""
            for x in range(3):
                word += data[si+di*x][sj+dj*x]

            if word not in SECOND_PATTERN:
                return 0
        return 1

    for i in range(n-2):
        for j in range(m-2):
            ans += check_second(i, j, data)
    
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

def part2_2(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':
                # Check the four positions we need around 'A'
                up_left_r, up_left_c = r-1, c-1
                down_right_r, down_right_c = r+1, c+1
                up_right_r, up_right_c = r-1, c+1
                down_left_r, down_left_c = r+1, c-1

                # Check if positions are in bounds
                ul_in = in_bounds(up_left_r, up_left_c)
                dr_in = in_bounds(down_right_r, down_right_c)
                ur_in = in_bounds(up_right_r, up_right_c)
                dl_in = in_bounds(down_left_r, down_left_c)

                if not (ul_in and dr_in and ur_in and dl_in):
                    # If any of them is out of bounds, can't form an X here
                    continue

                # Characters at those positions
                ul_char = grid[up_left_r][up_left_c]
                dr_char = grid[down_right_r][down_right_c]
                ur_char = grid[up_right_r][up_right_c]
                dl_char = grid[down_left_r][down_left_c]

                # Diagonal 1 (up-left and down-right) must have one 'M' and one 'S'
                diag1_set = {ul_char, dr_char}
                
                # Diagonal 2 (up-right and down-left) must have one 'M' and one 'S'
                diag2_set = {ur_char, dl_char}

                # Check sets to ensure they contain exactly 'M' and 'S'
                cond1 = diag1_set == {'M', 'S'}
                cond2 = diag2_set == {'M', 'S'}

                if cond1 and cond2:
                    count += 1

    return count

data = list(map(list, get_input(4).splitlines()))
print(f"Part 1 Solution: {part1(data)}")
print(f"Part 1 Solution: {part2_2(data)}")
