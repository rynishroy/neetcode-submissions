from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Initialize adjacency list
        adj = {c: set() for w in words for c in w}

        # Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            # Bug 1 Fix: Check if a longer word is a prefix of a shorter word
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
                
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}  # False = visited, True = visiting (current path)
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True  # Cycle detected
            visit[c] = False
            res.append(c)
            return False

        # Bug 2 Fix: Must call DFS on every character to cover disconnected components
        for c in adj:
            if dfs(c):
                return ""  # Return empty string if a cycle is found

        # Bug 3 Fix: Reverse after the result array has been populated
        res.reverse()
        return "".join(res)

        


            
        