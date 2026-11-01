class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits using string manipulation
        reversed_x = int(str(x)[::-1]) * sign
        
        # Check for 32-bit signed integer overflow boundaries
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x
