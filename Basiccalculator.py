n1 = int(input('Enter Number 1 : '))
n2 = int(input('Enter Number 2 : '))
op = input("Enter Operator : ")

if op == '+':
    print('Addition is : ',n1+n2)
elif op == '-':
    print('Subtraction is : ',n1-n2)
elif op == '*':
    print('Multiplication is : ',n1*n2)
elif op == '/':
    print('Divison is : ',n1/n2)
elif op == '%':
    print('Remainder is : ',n1%n2)
else:
    print('Invalid Operator')
