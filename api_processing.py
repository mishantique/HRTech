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
    # Используйте Proxy API для извлечения ключевой информации из описания
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": f'Извлеки основную информацию из: {description}'}]
    )
    # Возвращаем первый вариант ответа
    return response.choices[0].message.content.strip()

def process_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_data = []
    for item in data:
        vacancy_info = item['vacancy']
        # Извлекаем ключевую информацию для описания вакансии
        vacancy_info['key_info'] = extract_key_info(vacancy_info['description'])

        for resume_type in ['confirmed_resumes', 'failed_resumes']:
            for resume in item.get(resume_type, []):
                # Извлекаем ключевую информацию для каждого резюме
                    resume['key_info'] = extract_key_info(' '.join([
                        str(resume.get('about', '')),
                        ', '.join(map(str, resume.get('key_skills', []))),
                        '. '.join([str(exp['description']) for exp in resume.get('experienceItem', []) if exp['description'] is not None])
                    ]))

        new_data.append(item)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

# Пути к входному и выходному файлам
input_file = 'JSON/testing_api.json'  # Убедитесь, что путь правильный
output_file = 'JSON/processed_data.json'

# Запускаем обработку
process_data(input_file, output_file)
