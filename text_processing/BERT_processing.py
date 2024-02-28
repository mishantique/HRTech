from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import json

# Загрузка модели и токенизатора
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Функция для получения эмбеддинга текста
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(1)
    return embeddings

# Функция для вычисления косинусного сходства
def compute_similarity(embeddings1, embeddings2):
    return cosine_similarity(embeddings1, embeddings2)

# Загрузка и обработка данных
def match_resumes_to_vacancies(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Предполагаем, что данные уже предобработаны
    for item in data:
        vacancy_text = item['key_info']  # Текст вакансии
        vacancy_embedding = get_embedding(vacancy_text)
        
        for resume in item['confirmed_resumes']:
            resume_text = resume['key_info']  # Текст резюме
            resume_embedding = get_embedding(resume_text)
            
            # Расчет сходства между вакансией и резюме
            similarity = compute_similarity(vacancy_embedding, resume_embedding)
            print(f"Сходство между вакансией и резюме: {similarity}")

# Путь к файлу с данными
input_file = 'path_to_your_processed_json_file.json'

# Сопоставление резюме с вакансиями
match_resumes_to_vacancies(input_file)
