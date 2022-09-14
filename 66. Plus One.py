class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str, digits)
        s = ''.join(s)
        s = str(int(s)+1)
        res = list(map(int, str(s)))
        return res
