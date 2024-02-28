from dotenv import load_dotenv
import os
import openai
import json
from openai import OpenAI
from resume_processing import extract_key_info
# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значения Proxy API ключа
api_key = os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.proxyapi.ru/openai/v1",
)

def process_vacancies(input_file, output_file):
    
    '''Функция для извлечения ключевой информации из вакансий.
    Принимает на вход путь к директориям для файла с вакансиями и для возвращаемого файла.
    Возвращает JSON-файл с ключевой информации по вакансиям в виде структурированного предложения.'''
    
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_data = []  # Этот список будет содержать обработанную информацию о вакансиях

    for item in data:
        vacancy_info = item['vacancy']
        vacancy_uuid = vacancy_info['uuid']  # Извлекаем uuid вакансии
        description = vacancy_info['description']  # Извлекаем описание вакансии
        comment = vacancy_info['comment']  # Извлекаем комментарий к вакансии

        processed_description = extract_key_info(description)
        processed_comment = extract_key_info(comment)

        processed_item = {
            'vacancy_uuid': vacancy_uuid,
            'processed_description': processed_description,
            'processed_comment': processed_comment
        }

        new_data.append(processed_item)  # Добавляем обработанные данные по вакансии в общий список

    # Сохраняем обработанные данные в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

# Использование функции
input_file = '../JSON/train.json'  
output_file = '../JSON/processed_vacs'
process_vacancies(input_file, output_file)
