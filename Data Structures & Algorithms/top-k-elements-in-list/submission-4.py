import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        uniques = set(nums)
        counts = [set() for _ in range(len(nums)+1)]
        counts[0] = uniques
        dic = {}
        max_index = 0
        k_freqs = []
        
        for unique in uniques:
            dic[unique] = 0

        for num in nums:
            count_index = dic[num] #current count index
            counts[count_index + 1].add(num) #adds to the next index
            
            counts[count_index].remove(num) #removes from current index
            dic[num] = count_index + 1 # increments count to next index
            
            if count_index + 1 > max_index:
                max_index = count_index + 1
            
        print(counts)
        i = max_index

        while(k>0):
            for num in counts[i]:
                k_freqs.append(num)
                k -= 1
                if(k<=0):
                    break
            i -= 1    

        return k_freqs        


            

            
        