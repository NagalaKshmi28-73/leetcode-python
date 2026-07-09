class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum=max(candies)
        answer=[]

        for candy in candies:
           
             answer.append(candy + extraCandies >= maximum)
        
        return answer