# Now see, there are a few rules in converting infix to post:
# 1) If the expression does not have outermost brackets, then add outermost brackets
# Now we will pick one element from this expression, at a time->
# a) if its an operand (i.e. A, B, C, etc..), then add them to expression
# b) if its an operatlr (i.e +,-,/), then add them to the stack
# c) ok, so if we encounter an operator, which has more precedence then the operator in the stack
#       then we will pop out that operatorr and put it in the expression
# d) when we encounter a closing bracket, we will pop out all the elements from the stack, intt the
#       expression

# A + B - (C * D ^ F ) * X + Y # nooooo
# dont cpy OK

infix = (input ("enter the string"))

def precedence (ques):  
    if ques =="^":
        return 3
    if ques == "*" or ques=="/" :   
        return 2
    if ques == "+" or ques=="-":
        return 1    
 
def infix_to_postfix( question ):
    question = '('+question+')' 
    postfix = []
    stack = []
    for i in question:
        # FOR BRACKETS
        if i == "(":
            stack.append (i)
        if i == ")":
            L = opposite_bracket(stack, postfix)
            stack = L[0]
            postfix = L[1]

        # FOR OPERATORS
        if (i == "*" or i == "/" or i == "^" or i == "+" or i == "-"):
            if stack[-1] not in "^*+-/": 
                stack.append(i)

            if precedence(i)< precedence(stack[-1]):
               stack.append(i)

            if precedence(i)> precedence(stack[-1]): 
                postfix.append(stack[-1])  
                stack.remove(stack[-1])
                stack.append(i)
                # now operators is done

        # FOR OPERANDS
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :   
            postfix.append(i)
    
        print("%s %-20s  %-20s" % (i, ''.join(stack), ''.join(postfix)))
    return (postfix)

def opposite_bracket(stack,postfix):
    for i in stack: 
        if i=="(":
            return [stack,postfix]
        else:
            postfix.append(i)
            stack.remove (i)

print(infix_to_postfix (infix))
