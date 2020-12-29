class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        for i, v in enumerate(nums):
            if v in dct and i <= dct[v]:
                return True
            dct[v] = i + k
        return False
        