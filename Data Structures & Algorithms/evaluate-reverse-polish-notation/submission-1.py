class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if(token == '+' or token == '-' or token == '*' or token == '/'):
                secondOperator = stack.pop()
                firstOperator = stack.pop()
                if(token=='+'):
                    stack.append(firstOperator + secondOperator);
                elif (token=='-'):
                    stack.append(firstOperator - secondOperator);
                elif (token=='*'):
                    stack.append(firstOperator * secondOperator);
                elif (token=='/'):
                    stack.append(int(firstOperator / secondOperator))
            else:
                stack.append(int(token))
            

        return stack.pop();
        