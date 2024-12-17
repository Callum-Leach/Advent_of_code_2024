from aoc.utilities.fetch import get_input

def part1_2(data):
    # Parse the input into rules and updates
    lines = data.strip().splitlines()
    rules = []
    updates = []

    # We'll read the lines until we hit a line without '|' (which will indicate updates)
    reading_rules = True
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '|' in line and reading_rules:
            # It's a rule line
            X, Y = line.split('|')
            rules.append((int(X), int(Y)))
        else:
            # We have reached the updates section
            reading_rules = False
            updates.append(list(map(int, line.split(','))))

    # Function to check if a given update respects all applicable rules
    def check_update_order(rules, update):
        index_map = {p: i for i, p in enumerate(update)}
        for X, Y in rules:
            if X in index_map and Y in index_map:
                # X must appear before Y
                if index_map[X] > index_map[Y]:
                    return False
        return True

    total = 0
    for upd in updates:
        if check_update_order(rules, upd):
            mid_index = len(upd) // 2
            total += upd[mid_index]
    
    return total

def part2_2(data):
    lines = data.strip().splitlines()
    rules = []
    updates = []
    reading_rules = True
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '|' in line and reading_rules:
            X, Y = line.split('|')
            rules.append((int(X), int(Y)))
        else:
            reading_rules = False
            updates.append(list(map(int, line.split(','))))

    def check_update_order(rules, update):
        index_map = {p: i for i, p in enumerate(update)}
        for X, Y in rules:
            if X in index_map and Y in index_map:
                if index_map[X] > index_map[Y]:
                    return False
        return True

    def topological_sort(pages, rules):
        # Build adjacency and in-degree for pages involved
        pages_set = set(pages)
        adj = {p: [] for p in pages_set}
        in_degree = {p: 0 for p in pages_set}

        for X, Y in rules:
            if X in pages_set and Y in pages_set:
                adj[X].append(Y)
                in_degree[Y] += 1

        # Kahn's algorithm for topological sort
        queue = [p for p in pages_set if in_degree[p] == 0]
        sorted_pages = []

        while queue:
            # You can use a queue or just pop, order does not matter as long as it's consistent
            p = queue.pop()
            sorted_pages.append(p)
            for nxt in adj[p]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        # If sorted_pages doesn't contain all pages, there was a cycle. 
        # Problem doesn't mention this scenario, assuming no cycles in valid rules.
        return sorted_pages

    total = 0
    for upd in updates:
        if not check_update_order(rules, upd):
            # We need to reorder this update
            correct_order = topological_sort(upd, rules)
            mid_index = len(correct_order) // 2
            total += correct_order[mid_index]

    return(total)

data = get_input(5)
print(f"Part 1 Solution: {part1_2(data)}")
print(f"Part 2 Solution: {part2_2(data)}")
