class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open<n
        #only add closing paranthesis if closed<open
        #valid if openN==closedN==n
        
        stack=[]
        res =[]

        def backtracking(openN, closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append('(')
                backtracking(openN+1, closedN)
                stack.pop()
            
            if closedN<openN:
                stack.append(')')
                backtracking(openN,closedN+1)
                stack.pop()
        backtracking(0,0)
        return res

        