import json

# Открываем файл и считываем его содержимое
with open('C:/Users/МИХАИЛ/Desktop/Хакатоны/SENSE/JSON/train.json', 'r', encoding='utf-8') as f:
    json_data = f.read()

# Подсчитываем количество символов
num_characters = len(json_data)

print(f"Количество символов в JSON файле: {num_characters}")