class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hash_a,hash_b = {}, {}
            for i in range(len(s)):
                hash_a[s[i]] = 1 + hash_a.get(s[i],0)
                hash_b[t[i]] = 1 + hash_b.get(t[i],0)
            return hash_a == hash_b
        return False
        