class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = []
        t_letters = []

        for i in s:
            s_letters.append(i)
        for i in t:
            t_letters.append(i)

        s_sorted = sorted(s_letters)
        t_sorted = sorted(t_letters)

        if s_sorted == t_sorted:
            return True
        else:
            return False