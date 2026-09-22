class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs) == 1:
        #     return [strs]
        seen = {}
        result = []
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in seen:
                seen[sorted_str].append(strs[i])
            else:
                seen[sorted_str] = [strs[i]]
        for k, v in seen.items():
            result.append(v)
        return result
