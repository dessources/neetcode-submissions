class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        tuple_count = zip(count.values(),count.keys())
        return [t[1] for t in sorted(tuple_count,reverse=True)[:k]]
        