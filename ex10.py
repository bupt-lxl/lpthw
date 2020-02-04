# \   转义符, 结尾的\表示续行
# \n  换行
# \t  tab键
# \b  退格（backspace）
# \r  回车
# \v  纵向增加制表符
# \000  空
# \...  对其后的三位数字按ascII转义为字符
# \x..  用两位16进制数来表示一个字符

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
 
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
 
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)