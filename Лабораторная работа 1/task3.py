list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Общее количество игроков
total_players = len(list_players)

# Разделение на две равные команды
team1 = list_players[:total_players // 2]
team2 = list_players[total_players // 2:]

# Вывод результатов разделения участников по командам
print("Команда 1:", team1)
print("Команда 2:", team2)
