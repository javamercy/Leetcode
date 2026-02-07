import heapq
from collections import Counter
from select import select


class Solution:
    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [c[0] for c in counts][:k]

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        heap = []
        for key, value in counts.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [c[1] for c in heap]

    def topKFrequent3(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        max_freq = max(counts.values())
        bucket = [[] for _ in range(max_freq + 1)]
        for key, value in counts.items():
            bucket[value].append(key)
        return [item for sublist in bucket for item in sublist][-k:]
