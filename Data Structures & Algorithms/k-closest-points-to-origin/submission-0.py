import heapq
class Solution:
    
    def euclidean(self, p: List[int]):
        if len(p) != 2:
            return None
        
        return ((p[0] - 0)**2 + (p[1] - 0)**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for i,point in enumerate(points):
            point_dis = self.euclidean(point)
            if(i<=k-1):
                heapq.heappush_max(heap, (point_dis,point))
            else:
                print(heap[0])
                if(self.euclidean(heap[0][1]) > point_dis):
                    heapq.heapreplace_max(heap,(point_dis,point))

        final_heap = [item[1] for item in heap]
        return final_heap            




        

        