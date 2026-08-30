class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap={}
        for i,n in enumerate(nums):
            difference = target - n
            if(difference in nums_hashmap):
                return [nums_hashmap[difference],i]
            else:
                nums_hashmap[n]=i