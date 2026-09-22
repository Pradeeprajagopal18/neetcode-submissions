class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str =''
        for string in strs:
            encoded_str += str(len(string)) + '#'+ string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            count=int(s[i:j])
            string = s[j+1:j+1+count]
            decoded_list.append(string)
            i = j + 1 + count
        return decoded_list