from dotenv import load_dotenv
import os
import openai
import json
from openai import OpenAI

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значения Proxy API ключа
api_key = os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.proxyapi.ru/openai/v1",
)

def extract_key_info(description):
    # Используем Proxy API для извлечения ключевой информации из описания
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": f'''Извлеки основную информацию из: {description} 
                   и структурируй ответ таким образом:
                   "Предложение, содержащее информацию о технологическом стеке.
                   Предложение с информацией о наличии коммерческого опыта.
                   Предложение с информацией об образовании.
                   Предложение с возрастом.
                   Предложение с grade (сеньор/ миддл/ ..)
                   Предложение с предпочтениями удаленный формат работы/ офис.
                   Предложение с зарплатой.
                   Предложение с личными качествами.
                   Если что-то отсутствует, пиши в предложении NaN'''}]
    )
    # Возвращаем первый вариант ответа
    return response.choices[0].message.content.strip()

def process_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_data = []  # Этот список будет содержать только key_info для каждого резюме
    for item in data:
        processed_item = {}  # Создаем новый словарь для каждой вакансии

        for resume_type in ['confirmed_resumes', 'failed_resumes']:
            processed_item[resume_type] = []  # Инициализируем список для резюме данного типа

            for resume in item.get(resume_type, []):
                # Извлекаем и обрабатываем ключевую информацию для каждого резюме
                key_info = extract_key_info(' '.join([
                    str(resume.get('about', '')),
                    ', '.join(map(str, resume.get('key_skills', []))),
                    '. '.join([str(exp['description']) for exp in resume.get('experienceItem', []) if exp['description'] is not None])
                ]))
                processed_item[resume_type].append({'key_info': key_info})  # Сохраняем только key_info

        new_data.append(processed_item)  # Добавляем обработанные данные по вакансии в общий список

    # Сохраняем обработанные данные в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

# Пути к входному и выходному файлам
input_file = 'JSON/testing_api.json'  # Убедитесь, что путь правильный
output_file = 'JSON/processed_data.json'

# Запускаем обработку
process_data(input_file, output_file)
