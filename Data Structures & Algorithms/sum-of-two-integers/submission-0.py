class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        # If b is greater than 0, it means it didn't finish properly because of overflow 
        # (handling negative numbers in 32-bit format)
        return (a & mask) if b > 0 else a