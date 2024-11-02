class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i

        return []
    