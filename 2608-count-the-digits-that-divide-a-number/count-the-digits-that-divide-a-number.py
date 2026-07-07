class Solution:
    def countDigits(self, num: int) -> int:
        original=num
        count=0
        while num > 0:#7
            digit=num%10#7%10=7
            if original %digit==0:
                count+=1
            
            num//=10
        return count
