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


# Чтение исходного файла
with open('C:/Users/МИХАИЛ/Desktop/Хакатоны/SENSE/JSON/vacancies_only.json', 'r', encoding='utf-8') as file:
    
    '''Функция для выделения ключевой информации из JSON.
    Принимает на вход путь к директории с JSON-файлом 
    с неструктурированными данным. Возвращает JSON с ключевой информацией
    в виде структурированного текста.'''
    
    data = json.load(file)

# Создание нового списка с обновленной информацией
new_data = []
for item in data:
    key_info = extract_key_info(item['description'])
    new_data.append({
        'uuid': item['uuid'],
        'key_info': key_info
    })

output_file = 'JSON/vacancies_processed.json'
# Сохраняем обработанные данные в выходной файл
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)


