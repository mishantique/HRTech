import json

def sort_and_filter_similarities(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Сортировка данных по убыванию сходства и фильтрация нужных полей
    sorted_and_filtered_data = sorted(
        [{"resume_uuid": item['resume_uuid'], "similarity": item['similarity'][0][0]} for item in data], 
        key=lambda x: x['similarity'], 
        reverse=True
    )

    # Сохранение отсортированных и отфильтрованных данных в новый файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(sorted_and_filtered_data, out_file, ensure_ascii=False, indent=4)

# Путь к файлу с данными и к выходному файлу
input_file = 'text_processing/similaritites.json'
output_file = 'text_processing/sorted_similarities1.json'

# Вызов функции сортировки
sort_and_filter_similarities(input_file, output_file)