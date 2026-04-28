class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = 0
        for i in nums:
            for j in nums:
                if i == j:
                    seen += 1
            if seen > 1:
                return True
            else:
                seen = 0
        return False