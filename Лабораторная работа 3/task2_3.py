# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(group1, group2, separator=","):
    # Разделяем строки участников на списки по заданному разделителю
    group1_list = group1.split(separator)
    group2_list = group2.split(separator)

    # Ищем общих участников
    common_participants = sorted(set(group1_list) & set(group2_list))

    return common_participants

# Проверяем работу функции с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, separator="|")

# Вывод списка общих участников
print(common)