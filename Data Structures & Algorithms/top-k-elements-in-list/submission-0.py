class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map will have how many each
        # heap will have k most left.
        # for each element, push to heap. if len(heap) > k at any point, pop out the min value.
        # keep min heap with <= k items at all times. return this at the end


        import heapq

        res = []
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = seen.get(n, 0 ) + 1
        

        for n in seen:
            heapq.heappush(res, (seen[n], n))
            if len(res) > k:
                heapq.heappop(res)
        
        # print(res)
        out = []
        for i, n in res:
            out.append(n)
        return out
