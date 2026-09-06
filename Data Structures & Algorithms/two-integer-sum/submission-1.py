class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} 
        for i,n in enumerate(nums):
            numb=target-n
            if numb in map:
                return [map[numb],i]
            map[n]=i