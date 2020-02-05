# 更多用户输入提示
from sys import argv

script, name = argv
prompt = '> '

print(f"Hi {name}, I'm the {script} script.")

print(f"Do you like me {name}?")
likes = input(prompt)

print(f"Where do you live {name}?")
lives = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.
Nice!
""")
