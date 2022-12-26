number_tickets = int(input('Введите количество билетов:'))
age_list = [int(input(f"Введите возраст {i} - го посетителя:")) for i in range(1, number_tickets + 1)]
price_list = []
for age in age_list:
if age < 18:
price_list.append(0)
elif 18 <= age < 25:
price_list.append(990)
else:
price_list.append(1390)
order_cost = sum(price_list)
if len(price_list) > 3:
order_cost *= 0.9
print(order_cost)