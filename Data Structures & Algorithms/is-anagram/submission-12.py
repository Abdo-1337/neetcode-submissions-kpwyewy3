class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        t_lst = list(t)
        for i in s:
            if i not in t_lst:
                return False
            else:
                t_lst.remove(i)
        return True