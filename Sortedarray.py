class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        square_elements = []
        for item in A:
            prod = item*item
            square_elements.append(prod)
        square_elements.sort()
        return square_elements