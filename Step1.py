def calculate(op, num1, num2):
    if (op == '+'):
        return (input1 + input2)
    elif (op == '-'):
        return (input1 - input2)
    elif (op == 'X' or op == 'x'):
        return (input1 * input2)
    elif (op == '/'):
        return(input1 / input2)

#take three inputs
operators = ['+', '-', 'x', '/']
op = input("Enter one of the operator from ['+', '-', 'X', '/'] : ")
op = op.strip();
if(not (op in operators)):
    print( op + " is not valid operator.")
    exit()

try:
    input1 = int(input("Enter the first Number :"))
except ValueError :
    print("Not an integer! Try again.")

try:
    input2 = int(input("Enter the 2nd Number : "))
except ValueError :
    print("Not an integer! Try again.")

print ( 'Evaluating ' + str(input1) + ' ' + op +  ' ' + str(input2))

result = calculate(op, input1, input2 )

print('Result = ' + str(result))
