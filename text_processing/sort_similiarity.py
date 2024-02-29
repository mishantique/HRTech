import json

def sort_similarities_by_score(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Сортировка данных по убыванию сходства
    sorted_data = sorted(data, key=lambda x: x['similarity'][0][0], reverse=True)

    # Сохранение отсортированных данных в новый файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(sorted_data, out_file, ensure_ascii=False, indent=4)

# Путь к файлу с данными и к выходному файлу
input_file = 'TGGrXbXiuJZyiKyUVNnTujSAnABq9UmHAx'
output_file = '/mnt/data/sorted_similarities.json'

# Вызов функции сортировки
sort_similarities_by_score(input_file, output_file)