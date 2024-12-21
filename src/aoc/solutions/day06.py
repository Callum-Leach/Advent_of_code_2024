import time
from aoc.utilities.fetch import get_input

def part1_2(data):
    """
    Given a list of strings representing the map,
    returns the number of distinct positions the guard visits
    before leaving the map.
    """
    grid = data.strip().splitlines()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Directions in order: Up (^), Right (>), Down (v), Left (<)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    # Find the guard's initial position and orientation
    guard_r, guard_c = None, None
    direction_index = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in dir_map:
                guard_r, guard_c = r, c
                direction_index = dir_map[grid[r][c]]
                break
        if guard_r is not None:
            break

    visited = set()
    visited.add((guard_r, guard_c))

    while True:
        dr, dc = directions[direction_index]
        next_r = guard_r + dr
        next_c = guard_c + dc

        # Check if the next step is out of the map
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            # Guard leaves the map
            break

        # Check for obstacle
        if grid[next_r][next_c] == '#':
            # Turn right (no move this step)
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            guard_r, guard_c = next_r, next_c
            visited.add((guard_r, guard_c))

    return len(visited)

def part2_2(data):
    """
    Given a list of strings representing the map, returns how many
    distinct open cells could be turned into an obstacle '#' such that
    the guard ends up stuck in a loop.
    """
    grid = data.strip().splitlines()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Convert grid to list of lists for easier modification
    grid_list = [list(row) for row in grid]

    # Directions: Up (^), Right (>), Down (v), Left (<)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    # Find guard's initial position and direction
    guard_start_r, guard_start_c = None, None
    guard_dir_index = None

    for r in range(rows):
        for c in range(cols):
            if grid_list[r][c] in dir_map:
                guard_start_r, guard_start_c = r, c
                guard_dir_index = dir_map[grid_list[r][c]]
                break
        if guard_start_r is not None:
            break

    def simulate_with_obstacle(obst_r, obst_c):
        """
        Simulate the guard’s movement if we place an obstacle at (obst_r, obst_c).
        Return True if the guard ends up in a loop, otherwise False.
        """
        # Temporarily place the obstacle
        original_char = grid_list[obst_r][obst_c]
        grid_list[obst_r][obst_c] = '#'

        # Copy the guard’s initial state
        r = guard_start_r
        c = guard_start_c
        d_index = guard_dir_index

        # Track visited states: (row, col, direction_index)
        visited_states = set()
        visited_states.add((r, c, d_index))

        while True:
            dr, dc = directions[d_index]
            nr, nc = r + dr, c + dc

            # Check if out of bounds => guard leaves map => no loop
            if not (0 <= nr < rows and 0 <= nc < cols):
                # Restore original cell
                grid_list[obst_r][obst_c] = original_char
                return False

            # Check if next cell is blocked
            if grid_list[nr][nc] == '#':
                # Turn right
                d_index = (d_index + 1) % 4
            else:
                # Move forward
                r, c = nr, nc

            state = (r, c, d_index)
            if state in visited_states:
                # We have a repeated state => loop detected
                grid_list[obst_r][obst_c] = original_char
                return True
            visited_states.add(state)

    # Try placing the obstruction in each valid '.' cell
    loop_count = 0
    for r in range(rows):
        for c in range(cols):
            # We skip cells that are not '.' 
            # or that are the guard's initial cell
            if (grid_list[r][c] == '.' and not (r == guard_start_r and c == guard_start_c)):
                if simulate_with_obstacle(r, c):
                    loop_count += 1

    return loop_count

data = get_input(6)

# Part 1
start = time.time()
result_1 = part1_2(data)
end = time.time()
print(f"Part 1 took {end - start:.4f} seconds, result: {result_1}")

# Part 1 v1
start = time.time()
result_2 = part2_2(data)
end = time.time()
print(f"Part 2 took {end - start:.4f} seconds, result: {result_2}")
