class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c.lower() for c in s if (c.isalpha() or c in "0123456789")]
        return lst == lst[::-1]
        