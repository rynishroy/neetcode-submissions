class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left , right = max(weights), sum(weights)

        while left<right:
            mid = (left+right)//2

            current_weight = 0
            required_days = 1

            for w in weights:
                if current_weight +w >mid:
                    required_days +=1
                    current_weight =0
                current_weight +=w

            if required_days <=days:
                right =mid
            else:
                left =mid+1
        return left        