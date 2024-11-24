salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ...)

def calculate_sc(salary, spend, months, increase):
    # Начальное значение подушки
    required_capital = 0

    for month in range(months):
        # В первый месяц расходы без роста цен
        if month == 0:
            current_spend = spend
        else:
            # В последующих месяцах расходы увеличиваются на 3% ежемесячно
            current_spend = spend * (1 + increase) ** month

        # Вычисляем нехватку средств для покрытия расходов
        deficit = current_spend - salary

        # Если нехватка, добавляем её к подушке
        if deficit > 0:
            required_capital += deficit

    # Возвращаем значение
    return round(required_capital)

# Вычисляем необходимую подушку безопасности
money_capital = calculate_sc(salary, spend, months, increase)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
