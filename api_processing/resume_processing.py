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
    
    '''Функция принимает на вход информацию,
    которая содержится в каждой из записей в JSON.
    Возвращает содержимое сгенерированного ответа в виде строки.'''
    
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
    
    '''Функция для выделения ключевой информации из JSON.
    Принимает на вход путь к директории с JSON-файлом 
    с неструктурированными данным. Возвращает JSON с ключевой информацией
    в виде структурированного текста.'''
    
    
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_data = []  # Этот список будет содержать только uuid и key_info для каждого резюме
    for item in data:
        vacancy_uuid = item['vacancy']['uuid']  # Извлекаем uuid вакансии
        processed_item = {
            'vacancy_uuid': vacancy_uuid,
            'confirmed_resumes': [],
            'failed_resumes': []
        }  # Создаем новый словарь для каждой вакансии

        for resume_type in ['confirmed_resumes', 'failed_resumes']:
            for resume in item.get(resume_type, []):
                resume_uuid = resume['uuid']

                # Убедитесь, что key_skills и educationItem являются списками, иначе замените их на пустой список
                key_skills = resume.get('key_skills') or []
                education_items = resume.get('educationItem') or []

                # Обработка educationItem для получения строк
                education_info = ', '.join([str(education.get('specialty', '') + ' at ' + education.get('organization', ''))
                                            for education in education_items if education.get('specialty') is not None])

                # Обработка experienceItem для получения строк
                experience_info = '. '.join([exp['description'] for exp in resume.get('experienceItem', [])
                                            if exp.get('description') is not None])

                # Собираем все части в одну строку описания
                description = ' '.join([
                    str(resume.get('about', '')),
                    ', '.join(map(str, key_skills)),
                    education_info,
                    experience_info
                ])

                # Извлекаем ключевую информацию с помощью функции extract_key_info
                key_info = extract_key_info(description)

                # Добавляем информацию в список для соответствующего типа резюме
                processed_item[resume_type].append({
                    'resume_uuid': resume_uuid,
                    'key_info': key_info
                })

        new_data.append(processed_item)  # Добавляем обработанные данные по вакансии в общий список

    # Сохраняем обработанные данные в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

# Пути к входному и выходному файлам (Резюме)
input_file = 'JSON/train.json'  
output_file = 'JSON/processed_data.json'

# Запускаем обработку для резюме
process_data(input_file, output_file)

