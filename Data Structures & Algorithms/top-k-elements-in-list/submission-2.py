class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for i in range(len(nums)):
            if nums[i] in val:
                val[nums[i]] += 1
            else:
                val[nums[i]] = 1
        sorted_val = sorted(val.items(), key=lambda x: x[1], reverse=True)
        result = []
        for key,v in sorted_val:
            result.append(key)
            if len(result) == k:
                break
            
        return result            
        