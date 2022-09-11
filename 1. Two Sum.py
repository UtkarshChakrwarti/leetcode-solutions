class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        res = []
        for i in range(len(n)):
            sum = 0
            if n[i] >= 0:
                sum = t - n[i]
                if n[i+1:].count(sum) > 0:
                    res.append(i)
                    res.append(n[i+1:].index(sum)+len(n[0:i+1]))
                    return res
            if n[i] < 0:
                sum = n[i]*-1 + t
                if n[i+1:].count(sum) > 0:
                    res.append(i)
                    res.append(n[i+1:].index(sum)+len(n[0:i+1]))
                    return res
