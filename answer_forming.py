# Повторно импортируем необходимые модули и загружаем данные после сброса состояния выполнения кода
import json

# Загрузим и обработаем содержимое SORTED_ANSWER.json
file_path_sorted_answer = 'SORTED_ANSWER.json'

with open(file_path_sorted_answer, 'r', encoding='utf-8') as file:
    sorted_data = json.load(file)

# Вычислим количество элементов, составляющих первые 25%
quarter_length = len(sorted_data) // 4
selected_data = sorted_data[:quarter_length]

# Создадим новый JSON файл с комментарием и первыми 25% данных
output_data = {
    "comment": "Количество приемлемых вакансий определяется исследователем. Согласно статистическому анализу файла train_data, среднее количество принятых вакансий составляет около 25%. Опираясь на этот факт, оставим четверть из ранжированного списка. Ранжированный список находится в полном распоряжении рекрутера.",
    "data": selected_data
}

output_file_path = 'ANSWER.json'
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

output_file_path