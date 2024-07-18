print('Create your account')

username = input('Input username : ')
password = input('Input password : ')

print("user 'admin' created successfully")

print('Login now')
loginuser = input('Input username : ')
loginpassword = input('Inout password : ')

if (username == loginuser and password == loginpassword):
    print('User logged in successfully')
else :
    print('Invalid credentials')