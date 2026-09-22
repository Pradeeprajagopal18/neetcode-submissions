class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            print(values)
            print(nums[i])
            print(target-nums[i])
            if nums[i] in values:
                return [values[nums[i]],i]
            else:
                values[target-nums[i]]=i
        # for num in nums:
        #     if target - num

        