# happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        
        numbers = set()
        numbers.add(n)
        
        while n != 0 or numbers:
            sum = 0
            while n > 0:
                remainder = n % 10
                n = n // 10
                sum += remainder**2
            if sum == 1:
                return True
            if sum in numbers:
                return False
            
            n = sum
            numbers.add(n)
        
        return False