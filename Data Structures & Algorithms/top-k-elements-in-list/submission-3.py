class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        counts_arr = list(zip(counts.values(), counts.keys()))

        return [t[1] for t in sorted(counts_arr,reverse=True)][:k]
        