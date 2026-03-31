import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        dic = {}
        k_freqs = []

        for num in nums:
            if num in dic:
                dic[num] = dic.get(num) + 1
            else:
                dic[num] = 1

        for key in dic.keys():            
            heapq.heappush(heap,(-dic[key],key))

        for i in range(0,k):
            k_freqs.append(heapq.heappop(heap)[1])

        return k_freqs    
