# 读文件
# open(filename)打开文件
# file.read() 读取文件内容

from sys import argv
script, filename = argv
 
txt = open(filename)
 
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
 
txt_again = open(file_again)
print(txt_again.read())