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

def process_json_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Если предполагается, что данные содержат специфические разделы
    if 'resumes' in data:  # Пример ключа, содержащего интересующие нас данные
        for resume in data['resumes']:
            if 'key_info' in resume:
                resume['key_info'] = preprocess_text(resume['key_info'])

    
    # Сохранение обработанных данных
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
input_file = 'text_processing/resumes_processed_test.json'
output_file = 'text_processing/test_resumes_normalized.json'

process_json_data(input_file, output_file)