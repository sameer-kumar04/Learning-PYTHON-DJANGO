try :
    x = int(input('Enter Any Number : '))
    print(x)
except :  #when there is an error it will how this
    print('Something Went wrong')
else :   #if there is no error occurs and program executed sucessfully
    print('Everything executed Peacfully')
finally :  #printed in both cases if there is no or a error
    print('Try except finished')