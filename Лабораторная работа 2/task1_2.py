money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", ...)

def months_wd(money_capital, salary, spend, increase):
    months = 0  # Подсчет месяцев

    while money_capital >= 0:
        # В первый месяц расходы без увеличения
        if months == 0:
            current_spend = spend
        else:
            # Расходы с учетом роста цен
            current_spend = spend * (1 + increase) ** months

        # Расчет бюджета
        money_capital += salary - current_spend

        # Если подушка безопасности закончилась, выход из цикла
        if money_capital < 0:
            break

        months += 1

    return months

# Вычисление количества месяцев без долгов
months = months_wd(money_capital, salary, spend, increase)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print(f"Количество месяцев, которое можно протянуть без долгов: {months}")
