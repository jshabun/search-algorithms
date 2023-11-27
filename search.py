from typing import List, Tuple
import heapq

class SearchAlgorithm:

    # Implement Uniform search
    @staticmethod
    def uniform_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Helper function to check if a move is valid
        def is_valid_move(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '-1'

        # Find the starting position
        start_row, start_col = None, None
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 's':
                    start_row, start_col = i, j
                    break

        # Initialize priority queue with starting position
        priority_queue = []  
        heapq.heappush(priority_queue, (0, start_row, start_col))
        visited = set()
        count = 1

        # Uniform Search algorithm
        while priority_queue:
            cost, row, col = heapq.heappop(priority_queue)

            # Check if the target is found
            if grid[row][col] == 't':
                return 1, grid

            if (row, col) not in visited:
                visited.add((row, col))

                # Label visited nodes with numbers
                if grid[row][col] != 's':
                    grid[row][col] = str(count)
                    count += 1

                directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if is_valid_move(new_row, new_col):
                        new_cost = cost + 1
                        heapq.heappush(priority_queue, (new_cost, new_row, new_col))

        # Return -1 if the target is not found
        return -1, grid
        pass

    # Implement Depth First Search
    @staticmethod
    def dfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Helper function to perform DFS
        def dfs_helper(grid, row, column, stack):
            if grid[row][column] == 't':
                return True

            stack.append((row, column))

            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dr, dc in directions:
                n_row, n_column = row + dr, column + dc
                if 0 <= n_row < len(grid) and 0 <= n_column < len(grid[0]) and grid[n_row][n_column] != '-1' and (n_row, n_column) not in stack:
                    if dfs_helper(grid, n_row, n_column, stack):
                        return True

            return False

        # Find the starting position
        start_row, start_column = None, None
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 's':
                    start_row, start_column = i, j
                    break

        stack = []
        found = dfs_helper(grid, start_row, start_column, stack)
        num = 1

        # Label the visited nodes with numbers
        for i, j in stack[1:]:
            grid[i][j] = str(num)
            num += 1

        return (1 if found else -1), grid
        pass

    # Implement Breadth First Search
    @staticmethod
    def bfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Breadth First Search algorithm
        queue = []
        visited = set()
        start_row, start_col = None, None

        # Find the starting position
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 's':
                    start_row, start_col = i, j
                    queue.append((i, j))
                    visited.add((i, j))
                    break

        count = 1
        while queue:
            row, col = queue.pop(0)

            # Check if the target is found
            if grid[row][col] == 't':
                return 1, grid

            if grid[row][col] != 's':
                grid[row][col] = str(count)
                count += 1

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and grid[new_row][new_col] != '-1'
                    and (new_row, new_col) not in visited
                ):
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        # Return -1 if the target is not found
        return -1, grid
        pass
    
    # Implement Best First Search
    @staticmethod
    def best_first_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Best First Search algorithm
        start_row, start_col, end_row, end_col = None, None, None, None

        # Find the starting and ending positions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 's':
                    start_row, start_col = i, j
                elif grid[i][j] == 't':
                    end_row, end_col = i, j

        priority_queue = []
        heapq.heappush(priority_queue, (0, start_row, start_col))
        visited = set()
        count = 1

        while priority_queue:
            cost, row, col = heapq.heappop(priority_queue)

            # Check if the target is found
            if grid[row][col] == 't':
                return 1, grid

            if (row, col) not in visited:
                visited.add((row, col))

                # Label visited nodes with numbers
                if grid[row][col] != 's':
                    grid[row][col] = str(count)
                    count += 1

                directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                        and grid[new_row][new_col] != '-1'
                        and (new_row, new_col) not in visited
                    ):
                        heuristic = abs(new_row - end_row) + abs(new_col - end_col)
                        heapq.heappush(priority_queue, (heuristic, new_row, new_col))

        # Return -1 if the target is not found
        return -1, grid
        pass
    
    # Implement A* Search
    @staticmethod
    def a_star_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # A* Search algorithm
        start_row, start_col, end_row, end_col = None, None, None, None

        # Find the starting and ending positions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 's':
                    start_row, start_col = i, j
                elif grid[i][j] == 't':
                    end_row, end_col = i, j

        priority_queue = []
        heapq.heappush(priority_queue, (0, start_row, start_col, 0))
        visited = set()
        count = 1

        while priority_queue:
            f_cost, row, col, g_cost = heapq.heappop(priority_queue)

            # Check if the target is found
            if grid[row][col] == 't':
                return 1, grid

            if (row, col) not in visited:
                visited.add((row, col))

                # Label visited nodes with numbers
                if grid[row][col] != 's':
                    grid[row][col] = str(count)
                    count += 1 

                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                        and grid[new_row][new_col] != '-1'
                        and (new_row, new_col) not in visited
                    ):
                        g_cost_new = g_cost + 1
                        heuristic = abs(new_row - end_row) + abs(new_col - end_col)
                        f_cost_new = g_cost_new + heuristic
                        heapq.heappush(priority_queue, (f_cost_new, new_row, new_col, g_cost_new))

        # Return -1 if the target is not found
        return -1, grid
        pass
    
    # Implement Greedy Search
    @staticmethod
    def greedy_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Greedy Search algorithm
        start_row, start_col, end_row, end_col = None, None, None, None

        # Find the starting and ending positions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 's':
                    start_row, start_col = i, j
                elif grid[i][j] == 't':
                    end_row, end_col = i, j

        priority_queue = []
        heapq.heappush(priority_queue, (0, start_row, start_col))
        visited = set()
        count = 1
        min_heuristic = float('inf')
        min_row, min_col = start_row, start_col

        while priority_queue:
            heuristic, row, col = heapq.heappop(priority_queue)

            # Check if the target is found
            if grid[row][col] == 't':
                return 1, grid

            if (row, col) not in visited:
                visited.add((row, col))

                # Label visited nodes with numbers
                if grid[row][col] != 's':
                    grid[row][col] = str(count)
                    count += 1

                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                        and (new_row, new_col) not in visited
                    ):
                        heuristic = abs(new_col - end_col) + abs(new_row - end_row)
                        h_check = abs(min_row - end_row) + abs(min_col - end_col)

                        if (
                            heuristic < min_heuristic
                            and grid[new_row][new_col] != '-1'
                            and heuristic < h_check
                        ):
                            min_heuristic = heuristic
                            min_row, min_col = new_row, new_col

                heapq.heappush(priority_queue, (min_heuristic, min_row, min_col))

        # Return -1 if the target is not found
        return -1, grid
        pass


if __name__ == "__main__":

    example = [
        ['0', '0', '0', '0'],
        ['0', '-1', '-1', 't'],
        ['s', '0', '-1', '0'],
        ['0', '0', '0', '-1']
    ]
    example2 = [
        ['s', '0', '0', '0', '-1', '-1', '-1', '-1'],
        ['0', '0', '0', '0', '0', '-1', '-1', '-1'],
        ['-1', '-1', '0', '-1', '-1', '0', '0', '0'],
        ['-1', '0', '0', '0', '0', '0', '0', 't']
    ]
    example3 = [
        ['s', '0', '0', '-1', '0'],
        ['0', '-1', '0', '-1', 't'],
        ['0', '-1', '0', '0', '0'],
        ['0', '0', '0', '-1', '0'],
        ['0', '-1', '-1', '-1', '0']
    ]
    example4 = [
        ['s', '0', '0', '0', '0'],
        ['-1', '-1', '0', '0', '0'],
        ['t', '-1', '0', '0', '0'],
        ['-1', '0', '0', '-1', '0'],
        ['0', '-1', '0', '-1', '0']
    ]
    example5 = [
        ['0', '0', '0', '-1', '0'],
        ['0', '0', '0', '-1', '0'],
        ['s', '0', '0', '0', '0'],
        ['0', '0', '0', '-1', 't'],
        ['0', '0', '0', '-1', '0']
    ]
    
    example6 = [
       ['0', '0', '-1', '0', '0', '0', '0', '0', '0', '-1'],
       ['-1','0', '-1', '0', 't', '-1', '0', '0', '-1', '-1'],
       ['-1', '0', '-1', '0', '0', '0', '0', '-1', '0', '0'],
       ['-1', '0', '0', '0', '0', '0', '0', '-1', '0', '-1'],
       ['-1', '0', '-1', '0', '-1', '-1', '0', '-1', '-1', '-1'],
       ['-1', '0', '0', '0', '-1', '0', '0', '-1', '0', '-1'],
       ['-1', '0', '-1', '-1', '-1', '-1', '0', '0', '0', '-1'],
       ['-1', '0', '0', '-1', 's', '0', '0', '0', '-1', '0'],
       ['0', '-1', '0', '0', '0', '0', '0', '-1', '-1', '0'],
       ['0', '-1', '0', '0', '0', '0', '0', '0', '0', '0' ]
    ]

    found, final_state = SearchAlgorithm.greedy_search(example5)
    if found == 1:
        print("Target found!")
    else:
        print("Target not found.")

    for row in final_state:
        print(' '.join(row))
