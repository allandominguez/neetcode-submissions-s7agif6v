class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        need = len(t_count)
        window = defaultdict(int)
        have = 0
        min_str = s + "a"   # max length + 1
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            r_char = s[right]
            if r_char in t_count and window[r_char] == t_count[r_char]:
                have += 1
            while have == need:
                l_char = s[left]
                if l_char in t_count and window[l_char] == t_count[l_char]:
                    if (right - left + 1) < len(min_str):
                        min_str = s[left:right + 1]
                    have -= 1
                window[l_char] -= 1
                left += 1
        return min_str if min_str != (s + "a") else ""