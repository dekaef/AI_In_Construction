# TODO Напишите функцию для поиска индекса товара

# Функция для поиска индекса первого вхождения товара
def find_item_index(items_list, item_to_find):
    # Проверка наличия товара в списке
    if item_to_find in items_list:
        return items_list.index(item_to_find)  # Возвращаем индекс первого вхождения
    return None  # Если товар не найден, возвращаем None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
