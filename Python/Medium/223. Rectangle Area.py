class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if E >= C or A >= G or B >= H or F >= D:
            area = 0
        else:
            area = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        
        return (D - B) * (C - A) + (G - E) * (H - F) - area