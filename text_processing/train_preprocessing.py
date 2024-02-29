import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pymystem3 import Mystem

# Скачивание необходимых ресурсов NLTK
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text, language='russian'):
    # Удаление специальных символов и приведение к нижнему регистру
    text = re.sub(r'\W', ' ', text.lower())
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Лемматизация
    mystem = Mystem()
    lemmatized_text = mystem.lemmatize(text)
    
    # Токенизация
    word_tokens = word_tokenize(''.join(lemmatized_text))
    
    # Удаление стоп-слов
    stop_words = set(stopwords.words(language))
    filtered_text = [word for word in word_tokens if word not in stop_words]
    
    return ' '.join(filtered_text)


# Функция для обработки данных из JSON файла
def process_json_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Обработка каждой записи в JSON файле
    for item in data:
        if 'key_info' in item:
            item['key_info'] = preprocess_text(item['key_info'])
        if 'confirmed_resumes' in item:
            for resume in item['confirmed_resumes']:
                if 'key_info' in resume:
                    resume['key_info'] = preprocess_text(resume['key_info'])
        if 'failed_resumes' in item:
            for resume in item['failed_resumes']:
                if 'key_info' in resume:
                    resume['key_info'] = preprocess_text(resume['key_info'])
    
    # Сохранение обработанных данных в новый JSON файл
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Путь к исходному и выходному файлам
input_file = 'JSON/resumes/resumes_processed(train).json'
output_file = 'text_processing/resumes_normalized.json'

# Вызов функции обработки данных
process_json_data(input_file, output_file)
