class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add if open < n
        # only add closed if closed < open
        # return if open == closed == n

        res = []
        stack = []

        def backtrack(n_open, n_closed):
            if n_open == n_closed == n:
                res.append(''.join(stack))
                return

            if n_open < n:
                stack.append('(')
                backtrack(n_open + 1, n_closed)
                stack.pop()

            if n_closed < n_open:
                stack.append(')')
                backtrack(n_open, n_closed + 1)
                stack.pop()
        backtrack(0,0)
        
        return res
