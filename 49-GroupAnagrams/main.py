from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            d[sorted_key].append(s)
        return list(d.values())
