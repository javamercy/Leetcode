class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p = {}
        set_t = set()
        for c1, c2 in zip(s, t):
            c = p.get(c1)
            if c is None:
                if c2 in set_t:
                    return False
                p[c1] = c2
                set_t.add(c2)
            elif c != c2:
                return False
        return True
