class Solution:

    def add_binary(self, vector):
        final = False
        pointer = len(vector) - 1

        while (final == False and pointer > -1):
            if (vector[pointer] == 0):
                vector[pointer] = 1
                final = True
            else:
                vector[pointer] = 0

            pointer -= 1  

        return vector          

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        vector = [0] * len(nums)
        subs = []
        combination_i = 0

        while(combination_i < 2**len(nums)):
            sub = []
            for j in range(0,len(nums)):
                if(vector[j] == 1):
                    sub.append(nums[j])
            
            subs.append(sub)
            self.add_binary(vector)
            combination_i +=1

        return subs    
        
        