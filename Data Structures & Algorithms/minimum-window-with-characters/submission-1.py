class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for char in t:
            d[char] +=1
        
        formed =0 
        total = len(d)
        left = right =0
        len_string = float("inf")
        subl,subr =0,0

        while right<len(s):
            char = s[right]
            if char in d:
                d[char] -=1
                if d[char] == 0:
                    formed +=1
                
            while left<=right and formed == total:
                curr_length = right-left+1
                if curr_length<len_string:
                    len_string = curr_length
                    subl, subr = left, right+1
                char = s[left]
                if char in d:
                    if d[char] ==0:
                        formed -=1
                    d[char] +=1
                left +=1
            right+=1
        return "" if len_string == float("inf") else s[subl:subr]