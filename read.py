con_list = open("F:/python/pythonProject/India.txt","r") # "r" : for readable,"a" : for apending,"w" : for writing
# for i in con_list:
#     print(i)
print(con_list.readlines()[1])
con_list.close()   #Never forget to close the opened file