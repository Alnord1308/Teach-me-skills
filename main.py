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
print(sum/items)



# 3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
if (sum%1) == 0: # убирает остаток если он равен 0
    sum = int(sum)
    print(sum)
else:
    print(sum)
print()

# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%



a = 0
sum_copy = sum
for x in str(order_num):
    if x == "2" and a!=1:
        sum = sum*0.5
        a = 1
        print("Скидка 50% "+str(sum))

if sum==sum_copy:
    print("Скидки нет " + str(sum))




# 5. Если кол-во пицц в заказе меньше 2, то номер в очереди нужно сократить на 5
if items < 2:
    order_num=order_num-5
    print("Поздравляем, вас продвинули в очереди на 5 мест, перед вами еще "+str(order_num)+" человек")