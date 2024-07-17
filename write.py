#"w" : w stands for wirte , if there is no file of given name it will create a new file and then write in it, and given file is present it will get clear and new text will be added by using write
#"a" : a stands for append , if there is no file it will give error, and if file is present it will start adding afterwards

file = open("F:/python/pythonProject/India.txt","w")
file.write("\nHere is the new text ")