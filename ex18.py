# Functions
# 通过def关键字定义函数
# *args 数组，接收所以传入的参数

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("aaa","bbbb")
print_two_again("a","b")
print_one("a")
print_none()