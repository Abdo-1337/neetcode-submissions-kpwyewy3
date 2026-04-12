class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, num_1 in enumerate(nums):
            index_2 = index_1 + 1
            while index_2 < len(nums):
                if num_1 + nums[index_2] == target:
                    return [index_1, index_2]
                index_2 += 1