tickets = int(input('Введите количество билетов: '))
numbers_ages = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    numbers_ages.append(input_value)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    final_price = sum(map(price, numbers_ages))
discount_price = int(final_price * 0.9)
if tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "руб.")
else:
    print('Стоимость всех билетов: ', final_price, "руб.")
