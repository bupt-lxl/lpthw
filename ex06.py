# f-string and string.format()
# 带有空大括号{}的字符串可以使用format方法将变量作为参数传入{}中进行解析

types = 10
peo = 'people'
x = f"There are {types} types of {peo}." # f-string中可以包含任意多个变量

print(x)
print(f"I said: {x}")

# 带有空大括号{}的字符串可以使用format方法将变量作为参数传入{}中进行解析
hilarious = 'hahaha!'
joke = "Isn't that joke so funny?! {}"
print(joke.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"
print(w + e)