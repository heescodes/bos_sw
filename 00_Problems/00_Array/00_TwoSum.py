class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
        num_map={}

#1. Dictionary : Optionally get key and value
                #for k in num_map.keys()
                #for v in num_map.values()

        for i, num in enumerate(nums):
            #List : i는 Index, num은 Value            
            cpl = target - num
            if cpl in num_map:
                return [i,num_map[cpl]]
            num_map[num]=i # Matching Value and Key 
        return []
