class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        last = []
        for num in nums:
            if num in last:
                return True
            last.append(num)
        return False
         