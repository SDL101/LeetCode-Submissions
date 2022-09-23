class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets =[[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for n, f in freq.items():
            buckets[f].append(n)
        
        output = []
        for b in range(len(buckets)-1, 0, -1):
            for each in buckets[b]:
                output.append(each)
                if len(output) == k:
                    return output
                
                
            
        