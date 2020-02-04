# 通过argv获取运行程序时携带的参数，
# argv为一个数组，其中argv[0]为文件名，后续依次为输入的参数

from sys import argv
print('argv: ', argv) #  argv:  ['ex13.py', '1', '2', '3']
# name = argv[0]
# first = argv[1]
# second = argv[2]
# third = argv[3]
name, first, second, third = argv # 解构赋值

print("The script is called:", name)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
