class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        last = set()
        for num in nums:
            if num in last:
                return True
            last.add(num)
        return False
         