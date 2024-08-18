class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)
        for num, freq in counts.items():
            buckets[freq].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            bucket = buckets[i]
            if len(bucket) > 0:
                for each in bucket:
                    res.append(each)
                if len(res) == k:
                    return res