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
        model="gpt-4", 
        messages=[{"role": "user", "content": f'''Извлеки информацию из: {description} 
                   и структурируй ответ таким образом:
                   "информацию о технологическом стеке.
                   информацией о наличии коммерческого опыта.
                   с информацией об образовании.
                   с grade (сеньор/ миддл/ ..)
                   с личными качествами.
                   Постарайся извлечь исчерпывающую информацию (как можно больше).
                   Рассматривай каждое резюме только в собственном контексте'''}]
    )
    # Возвращаем первый вариант ответа
    return response.choices[0].message.content.strip()

def process_data_test(input_file, output_file):
    """
    Функция для выделения ключевой информации из JSON.
    Принимает на вход путь к директории с JSON-файлом с неструктурированными данными.
    Возвращает JSON с ключевой информацией в виде структурированного текста.
    """
        # Чтение данных из исходного файла
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    print("Файл успешно открыт!")

    # Применение функции к описанию вакансии
    vacancy_description = data['vacancy']['description']
    vacancy_info = extract_key_info(vacancy_description)
    data['vacancy']['extracted_info'] = vacancy_info  # Добавляем извлеченную информацию к вакансии

    # Создание нового списка резюме, содержащего только 'uuid' и 'key_info'
    new_resumes = []
    for resume in data['resumes']:
        print('Перешли к новому резюме')
        resume_description = resume['about']  # Использование поля 'about' в качестве примера для извлечения
        key_info = extract_key_info(resume_description)  # Извлечение ключевой информации
        print('Работа с API openai отлажена.')
        new_resumes.append({
            "uuid": resume['uuid'],
            "key_info": key_info  # Использование нового названия поля
        })

    # Замена старого списка резюме новым
    data['resumes'] = new_resumes

    # Сохранение обновленных данных в новый JSON-файл
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Пути к входному и выходному файлам (Тестовый корпус)
input_file = 'JSON/compression/test_compressed.json'  
output_file = 'JSON/resumes/resumes_processed(test).json'
# Пример вызова функции
process_data_test(input_file, output_file)



