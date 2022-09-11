class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        for i in range(len(nums)):
            left = sum(nums[:i])

            if left == total-left-nums[i]:
                return(i)
        return -1
