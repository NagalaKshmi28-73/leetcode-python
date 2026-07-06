from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)      # Frequency of characters in p
        window = Counter()        # Frequency of current window
        result = []

        left = 0

        for right in range(len(s)):
            # Add current character to the window
            window[s[right]] += 1

            # Keep the window size equal to len(p)
            if right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            # Compare the two frequency maps
            if window == p_count:
                result.append(left)

        return result