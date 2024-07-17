def check(num):
    if( num & 1 == 0):
        print(num, ' is Even')
    else:
        print(num, ' is Odd')

num = int(input('Enter a Number : '))
print(check(num))