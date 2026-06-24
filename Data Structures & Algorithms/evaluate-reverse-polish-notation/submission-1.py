class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t in operators:
                i = int(stack.pop())
                j = int(stack.pop())
                match t:
                    case "+":
                        stack.append(int(i) + int(j))
                    case "-":
                        stack.append(int(j) - int(i))
                    case "*":
                        stack.append(int(i) * int(j))
                    case "/":
                        stack.append(int(j) / int(i))
            else:
                stack.append(t)
        return int(stack[-1])   