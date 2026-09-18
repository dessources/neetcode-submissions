class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        last = (ROWS-1, ROWS-1)

        seen = set()
        heap = [(grid[0][0], (0, 0))]
 
        while heap:
            time, (i, j) = heapq.heappop(heap)
            if (i, j) in seen:
                continue

            seen.add((i, j))
            if (i, j) == last:
                return time

            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x, y = i+di, j+dj
                if x < 0 or x == ROWS or y < 0 or y == COLS :
                    continue
                new_time = max(time, grid[x][y])
                heapq.heappush(heap, (new_time, (x, y)))