# for-in循环
# for item in list:
# for i in range(0, 6): 循环0,1,2,3,4,5
# list.append(item) 向列表末尾添加一个元素
# list.pop()
# del list[index]
# list.insert(index, item)

count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")