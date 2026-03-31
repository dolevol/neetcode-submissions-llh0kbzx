class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftovers = dict()

        for i, num in enumerate(nums):
            leftovers[target - num] = i     
        print(leftovers)
        for i, num in enumerate(nums):
            
            if(num in leftovers and i != leftovers.get(num)):
                print(i,num)
                return [i,leftovers[num]]

        print(leftovers)
        return  [1,1]      