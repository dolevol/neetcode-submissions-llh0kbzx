class Solution:
    def search(self, nums: List[int], target: int) -> int:
        


        # loop until high and low are the same
        # 
        
        high = len(nums) - 1
        low = 0
        mid = (high + low) // 2

        while(low <= high):
                print(nums[mid], "index:", mid)
                if(nums[mid] == target):
                        return mid

                elif(nums[mid] > target):
                        high = mid - 1

                else:
                        low = mid + 1

                mid = (high + low) // 2

        return -1