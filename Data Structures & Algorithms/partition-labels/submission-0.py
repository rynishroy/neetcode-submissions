class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcurrenceOfChar ={}

        for i, c in enumerate(s):
            lastOcurrenceOfChar[c] = i
        
        res =[]
        size =0
        end =0
        for i, c in enumerate(s):
            size +=1
            end =max(end, lastOcurrenceOfChar[c])

            if i==end:
                res.append(size)
                size = 0
        return res

        