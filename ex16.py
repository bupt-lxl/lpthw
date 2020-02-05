# Reading and Writing Files
# file.close() 关闭文件
# file.read() 读取文件内容
# file.readline() 按行读取文件内容
# file.truncate() 清空文件内容 
# file.write(content)  写入文件
# file.seek(offset)  移动文件读取指针到指定位置

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.seek(0)
target.write('insert')

print("And finally, we close it.")
target.close()