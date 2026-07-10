class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maximum = count

        # Sliding window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            maximum = max(maximum, count)

        return maximum
        