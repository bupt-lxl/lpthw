# 函数传参的不同方式

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")

cheese_and_crackers(20, 30) # 直接传入参数

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers) # 传入变量

cheese_and_crackers(10 + 20, 5 + 6) # 可计算得到参数
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # 组合形式