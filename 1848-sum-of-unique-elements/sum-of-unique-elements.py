from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)

        total = 0
        for num in count:
            if count[num] == 1:
                total += num

        return total