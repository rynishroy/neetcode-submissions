class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        res =[]
        def dfs(i, curr, target):
            if target == 0:
                res.append(curr.copy())
            if target <=0:
                return
            
            prev = -1
            for idx in range(i,len(candidates)):
                if candidates[idx] == prev:
                    continue
                curr.append(candidates[idx])
                dfs(idx+1, curr, target-candidates[idx])
                curr.pop()
                prev=candidates[idx]
        dfs(0,[],target)
        return res


            
                
        