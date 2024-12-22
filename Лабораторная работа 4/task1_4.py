# TODO решите задачу
import json

def calculate_sum_from_json(file_path):
    try:
        # Открытие и чтение файла
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Проверка данных
        if not isinstance(data, list):
            raise ValueError("JSON файл должен содержать список словарей.")

        # Вычисление суммы произведений
        total_sum = 0.0
        for item in data:
            if isinstance(item, dict):
                score = item.get("score", 0.0)
                weight = item.get("weight", 0.0)

                if isinstance(score, (int, float)) and isinstance(weight, (int, float)):
                    total_sum += score * weight
                else:
                    raise ValueError("Значения 'score' и 'weight' должны быть числовыми.")

        # Округление результата
        return round(total_sum, 3)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

# Пример использования
file_path = "input.json"  # Укажите путь к вашему JSON файлу
result = calculate_sum_from_json(file_path)
if result is not None:
    print(f"Сумма произведений: {result}")
