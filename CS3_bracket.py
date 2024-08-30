#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#Let the user input the string.

#Write a program to determine if the input string is balanced or not balanced
#Input String is balanced if,

#For every opening bracket, there is a closing bracket of the same type.
#All brackets are closed in the correct order 
#For this lab, we will use a stack as the data structure.

stack = [] #creates an empty stack


#Ask the user to input a string
s = input("Enter a string (must include '(', ')', '{', '}', '[' and ']') expression:")


#Check if the input string is balanced
for i in s: #traverse the string
    if i in ['(', '{', '[']: #if the character is an opening bracket, push it to the stack
    #== '(' or i =='{' or i == '[': #if the character is an opening bracket, push it to the stack
        stack.append(i)
    else:
        if not stack:
            print("The input string doesn't contain balanced brackets.")
            break
        else:
            current_char = stack.pop()
            if current_char == '(':
                if i != ')':
                    print("The input string doesn't contain balanced brackets.")
                    break
                else:
                    print("The input string contains balanced brackets.")
                    break
            if current_char == '{':
                if i != '}':
                    print("The input string doesn't contain balanced brackets.")
                    break
                else:
                    print("The input string contains balanced brackets.")
                    break
            if current_char == '[':
                if i != ']':
                    print("The input string doesn't contain balanced brackets.")
                else:
                    print("The input string contains balanced brakcets.")
                    break       
            



        
        