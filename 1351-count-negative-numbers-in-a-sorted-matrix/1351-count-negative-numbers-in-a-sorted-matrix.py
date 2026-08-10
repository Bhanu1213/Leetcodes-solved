class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for li in grid:
            count+=len([i for i in li if i<0])
        return count
        