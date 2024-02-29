import json

# Загрузка исходных данных из файла, находящегося в подпапке
with open('JSON/train.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Извлечение только данных о вакансиях
vacancies = [item['vacancy'] for item in data]

# Сохранение данных о вакансиях в новый файл, также в подпапке JSON
with open('JSON/vacancies_only.json', 'w', encoding='utf-8') as file:
    json.dump(vacancies, file, ensure_ascii=False, indent=4)
