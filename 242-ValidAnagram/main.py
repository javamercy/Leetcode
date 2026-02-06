from collections import defaultdict, Counter


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = defaultdict(int)
        for l in s:
            dict_s[l] += 1

        dict_t = defaultdict(int)
        for l in t:
            dict_t[l] += 1

        if len(dict_s.keys()) != len(dict_t.keys()):
            return False

        return dict_s == dict_t

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram3(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram4(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = defaultdict(int)
        for char in s:
            d[char] += 1

        for char in t:
            d[char] -= 1
            if d[char] < 0:
                return False
        return True


print(Solution().isAnagram1("abaa", "aaba"))
