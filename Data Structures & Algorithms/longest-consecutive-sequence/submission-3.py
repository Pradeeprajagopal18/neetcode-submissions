class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        longest_len = 1
        current_len = 1
        num = sorted_nums[0]
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] == num:
                continue
            elif sorted_nums[i] == num+1:
                current_len += 1
            else:
                current_len = 1
            longest_len = max(longest_len, current_len)
            num = sorted_nums[i]
        return longest_len