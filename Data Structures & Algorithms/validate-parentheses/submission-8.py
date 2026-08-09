class Solution:
    def isValid(self, s: str) -> bool:
        arr = list(s);
        stack = [];

        for char in s:
            if(char=="{" or char=="[" or char=="("):
                stack.append(char);
            
            elif(char=="}" or char=="]" or char==")"):
                if not stack:
                    return False
                elif (char == "]" and stack[-1] != "[" or char == "}" and stack[-1] != "{") or char == ")" and stack[-1] != "(":
                    return False
                stack.pop()
        return not stack

