class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #stack to store all the INTS needed for this arithmetic
        operators = ["+", "-", "*", "/"] #all possible operators
        for t in tokens:
            if t in operators: #if the token is an operator
                right = int(stack.pop()) #the right one is counterintuitively the first one popped off
                left = int(stack.pop()) #left one is the SECOND one popped off
                match t: #python syntax for a switch statement
                    case "+":
                        stack.append(left + right)
                    case "-":
                        stack.append(left - right)
                    case "*":
                        stack.append(left * right)
                    case "/":
                        stack.append(int(left / right))
            else:
                stack.append(int(t)) #append the number to the stack if its not an operator
        return stack[-1] #there should only be one number left in the stack, the result of the operations