def solution(S):
    # Maximum allowed value for 20-bit unsigned integers
    MAX_VALUE = 2**20 - 1  # 1048575
    
    
    # Initialize an empty stack
    stack = []
    
    # Split the string into individual operations
    operations = S.split()
    
    # Loop through each operation
    for op in operations:
        if op.isdigit():  # If the operation is a number
            stack.append(int(op))  # Push it onto the stack
        elif op == "POP":  # If the operation is POP
            if not stack:  # If stack is empty, return -1
                return -1
            stack.pop()  # Remove the top element
        elif op == "DUP":  # If the operation is DUP
            if not stack:  # If stack is empty, return -1
                return -1
            stack.append(stack[-1])  # Duplicate the top element
        elif op == "+":  # If the operation is +
            if len(stack) < 2:  # If there are fewer than 2 elements
                return -1
            a = stack.pop()  # Pop the top element
            b = stack.pop()  # Pop the next element
            result = a + b  # Add them
            if result > MAX_VALUE:  # If the result exceeds the max value
                return -1
            stack.append(result)  # Push the result back onto the stack
        elif op == "-":  # If the operation is -
            if len(stack) < 2:  # If there are fewer than 2 elements
                return -1
            a = stack.pop()  # Pop the top element
            b = stack.pop()  # Pop the next element
            result = a - b  # Subtract them
            if result < 0:  # If the result is negative
                return -1
            stack.append(result)  # Push the result back onto the stack
        else:
            return -1  # Return -1 for any unknown operation
    
    # If the stack is empty after all operations, return -1
    if not stack:
        return -1
    
    # Return the top element of the stack
    return stack[-1]

# Example test cases
print(solution("4 5 6 - 7 +")) # Output: 8
print(solution("13 DUP 4 POP 5 DUP + DUP + -")) # Output: 7
print(solution("5 6 + -")) # Output: -1
print(solution("3 DUP 5 - -")) # Output: -1
print(solution("1048575 DUP +")) # Output: -1
