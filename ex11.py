
# input() 用户输入接口
# 用户输入的类型为String，可通过int()转为数字

print("How old are you?")
age = input()

print("How tall are you?", end=' ')
height = input()

print("How much do you weigh?", end=' ')
weight = input()

print("you're {} old, {} tall and {} heavy.".format(age, height, weight))
