class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res_list = []
        
        for i in range(len(nums)-1):
            res_list.append(nums[i] + nums[i+1])

        if len(res_list) != len(set(res_list)):
            return True
            
        else:
            return False
        
