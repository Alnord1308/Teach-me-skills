import os
from dotenv import load_dotenv

load_dotenv()

items = int(os.getenv('ITEMS'))
sum = float(os.getenv('SUM'))
order_num = int(os.getenv('ORDER_NUM'))

# ITEMS = 4
# SUM = 2.7
# ORDER_NUM = 684

print(type(items))
print(type(sum))
print(type(order_num))
print()



# 1. Касса перепутала номер в очереди с суммой. Надо поменять эти переменные местами
print("sum = "+str(sum)+"; order_num = "+str(order_num))
order_num, sum = sum, order_num # меняем местами номер в очереди с суммой
print("sum = "+str(sum)+"; order_num = "+str(order_num))
order_num, sum = sum, order_num # меняем обратно, чтобы не путаться






# 2. Для отчёта боссу, нужно посчитать среднюю стоимость каждой пиццы в заказе


# 3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
if (sum%1) == 0: # убирает остаток если он равен 0
    sum = int(sum)
    print(sum)
else:
    print(sum)

# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%


# 5. Если кол-во пицц в заказе меньше 2, от номер в очереди нужно сократить на 5
