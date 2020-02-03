# Formatting string with 'f' or 'F'
# 字符串前加F或f，会对其后的字符串进行格式化处理，{}里面的内容会被按变量进行解析
name = 'liuxiangli'
age = 27
height = 165
eyes = 'blue'

print(f"My name is {name}")
print(f"I'm {age} years old.")
print(f'I am {height}cm tall.')
print(f"I'm got {eyes} eyes.")
print(F"I'm got {eyes} eyes.") # F或f都可以
print(f"I'm learning English.")