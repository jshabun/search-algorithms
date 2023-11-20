from typing import List, Tuple
import heapq

class SearchAlgorithm:

    # Implement Uniform search
    @staticmethod
    def uniform_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        rows, columns = len(grid), len(grid[0])

        # Helper function to check if a cell is valid and not visited
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < columns and grid[x][y] != '-1'

        # Find the starting position 's'
        for i in range(rows):
            if 's' in grid[i]:
                start_x, start_y = i, grid[i].index('s')
                break

        # Initialize priority queue with the starting point
        priority_queue = [(0, start_x, start_y)]
        heapq.heapify(priority_queue)

        order = 1  # Counter for marking the order of visited cells

        while priority_queue:
            cost, x, y = heapq.heappop(priority_queue)

            if grid[x][y] == 't':
                return 1, grid

            if grid[x][y] == '0':
                grid[x][y] = str(order)
                order += 1

            # Explore neighbors (Right, Down, Left, Up)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy

                if is_valid(new_x, new_y):
                    new_cost = cost + 1
                    heapq.heappush(priority_queue, (new_cost, new_x, new_y))

        return -1, grid  
        #pass

    # Implement Depth First Search
    @staticmethod
    def dfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        
        pass
    
    # Implement Breadth First Search
    @staticmethod
    def bfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
    # Implement Best First Search
    @staticmethod
    def best_first_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
    # Implement A* Search
    @staticmethod
    def a_star_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
    # Implement Greedy Search
    @staticmethod
    def greedy_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass

if __name__ == "__main__":

    example = [
        ['0', '0', '0', '0'],
        ['0', '-1', '-1', 't'],
        ['s', '0', '-1', '0'],
        ['0', '0', '0', '-1']
    ]
    #example = [
    #    ['0', '0', '-1', '0', '0', '0', '0', '0', '0', '-1'],
    #    ['-1',' 0', '-1', '0', 't', '-1', '0', '0', '-1', '-1'],
    #    ['-1', '0', '-1', '0', '0', '0', '0', '-1', '0', '0'],
    #    ['-1', '0', '0', '0', '0', '0', '0', '-1', '0', '-1'],
    #    ['-1', '0', '-1', '0', '-1', '-1', '0', '-1', '-1', '-1'],
    #    ['-1', '0', '0', '0', '-1', '0', '0', '-1', '0', '-1'],
    #    ['-1', '0', '-1', '-1', '-1', '-1', '0', '0', '0', '-1'],
    #    ['-1', '0', '0', '-1', 's', '0', '0', '0', '-1', '0'],
    #    ['0', '-1', '0', '0', '0', '0', '0', '-1', '-1', '0'],
    #    ['0', '-1', '0', '0', '0', '0', '0', '0', '0', '0' ]
    #]

    found, final_state = SearchAlgorithm.uniform_search(example)
    if found == 1:
        print("Target found!")
    else:
        print("Target not found.")

    for row in final_state:
        print(' '.join(row))
