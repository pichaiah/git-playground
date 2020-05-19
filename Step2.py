def calculate(op, input1, input2):
    if (op == '+'):
        return (input1 + input2)
    elif (op == '-'):
        return (input1 - input2)
    elif (op == 'X' or op == 'x'):
        return (input1 * input2)
    elif (op == '/'):
        return(input1 / input2)


f = open("step_2.txt" , 'r')
total = 0
for line in f :
    line = line.rstrip('\n')
    print(line)
    arr =  line.split(' ')
    print('Evaluating ' + arr[2] + ' ' + arr[1] + ' ' + arr[3])
    total  = total +  int(calculate(arr[1], float(arr[2]), float(arr[3])))
    print( "Total = " + str(total))


