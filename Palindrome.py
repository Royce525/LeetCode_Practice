class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x #Stored into a temporary variable
        reverse = 0
        if x < 0:
            return False
        while x != 0:
            reverse = (reverse*10) + x % 10
            x = x // 10
        
        if temp == reverse:
            return True
        return False
