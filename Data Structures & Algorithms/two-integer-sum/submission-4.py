class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        results = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in results:
                return [results[val],i]
            results[nums[i]] = i
        return []
