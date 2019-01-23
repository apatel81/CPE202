#CPE 202 - Project 2
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian


from stack_array import *


class PostfixFormatException(Exception):
    pass


#To test for a valid or invalid postfix expression
#str(postfix) --> True or False
def postfix_valid(input_str):
    operandStack = StackArray(30)
    tokenList = input_str.split()
    
    for token in tokenList:
        if not token.isdigit():
           raise PostfixFormatException('Invalid Token')


#To take in a postfix expression and return the result of the evaluation of the expression
#str --> int
def postfix_eval(input_str):
    operandStack = StackArray(30)
    tokenList = input_str.split()
    operand_count = 0
    operator_count = 0

    for token in tokenList:
        if token.isdigit():
           operand_count += 1
        else:
           operator_count += 1

    if operand_count <= operator_count:
       raise PostfixFormatException('Insufficient operands')
    elif operand_count != (operator_count + 1):
       raise PostfixFormatException('Too many operands')

    else:
       for token in tokenList:
           if token.isdigit():
              operandStack.push(int(token))
              operand_count += 1
           else:
              operand2 = operandStack.pop()
              operand1 = operandStack.pop()
              result = do_math(token,operand1,operand2)
              operandStack.push(result)

    return operandStack.pop()


#To calculate basic arithmetic problems by priority 
#str(operator) int int --> int
def do_math(op, op1, op2):
    if op == "^":
       return op1 ** op2
    elif op == "*":
       return op1 * op2
    elif op == "/":
       if op2 == 0:
          raise ValueError('Cannot divide by 0')
       else:
          return op1 / op2
    elif op == "+":
       return op1 + op2
    elif op == "-":
       return op1 - op2
               

#To convert an infix expression to an equivalent postfix expression
#str(prefix) --> str(postfix)
def infix_to_postfix(input_str):
    opStack = StackArray(30)
    postfixlist = []
    tokenList = input_str.split()
    precedence = {}
    precedence["^"] = 4
    precedence["/"] = 3
    precedence["*"] = 3
    precedence["-"] = 2
    precedence["+"] = 2
    precedence["("] = 1

    for token in tokenList:
        if token.isdigit():
           postfixlist.append(token)
        elif token == '(':
           opStack.push(token)
        elif token == ')':
           top_token = opStack.pop()
           while top_token != '(':
              postfixlist.append(top_token)
              top_token = opStack.pop()

        else:
           while (not opStack.is_empty()) and (precedence[token] <= precedence[opStack.peek()]):
                 if token == '^':
                    break
                 else:
                    postfixlist.append(opStack.pop())
           opStack.push(token)

    while not opStack.is_empty():
          postfixlist.append(opStack.pop())
   
    return " ".join(postfixlist)


#To convert a prefix expression to an equivalent postfix expression
#str(prefix) --> str(postfix)
def prefix_to_postfix(input_str):
    opStack = StackArray(30)
    postfixlist = []
    tokenList = input_str.split()

    for token in range(len(tokenList)-1, -1, -1):
        if tokenList[token].isdigit():
           opStack.push(tokenList[token])
        else:
           op1 = opStack.pop()
           op2 = opStack.pop()
           str_list = [op1 , op2 , tokenList[token]]
           new_str = " ".join(str_list)
           opStack.push(new_str)

    return opStack.pop()
 
