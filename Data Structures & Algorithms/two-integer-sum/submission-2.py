class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        # for i in range(len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        seen = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in seen:
                return [seen[num],i]
            seen[nums[i]] = i
        return [] 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i in range(len(nums)):
#             needed = target - nums[i]
#             if needed in seen:
#                 return [seen[needed], i]
#             seen[nums[i]] = i
#         return []