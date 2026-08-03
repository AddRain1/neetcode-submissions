class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # iterate through each token
        # add two integers to stack
        # when operator encountered, pop two ints and append result
        # stack should only contain result at the end

        stack = []
        operators = {"+", "*", "-", "/"}
        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
                
            else:
                stack.append(int(token))
        
        return stack[0]

