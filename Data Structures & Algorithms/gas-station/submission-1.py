class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #theres should be enough gas
        if sum(gas)<sum(cost):
            return -1
        total =0
        start =0
        #loop through the ga and calucate the difference if the differnce is <0 then start at next index
        for i in range(len(gas)):
            total +=(gas[i]-cost[i])

            if total<0:
                total =0
                start =i+1
        return start
        