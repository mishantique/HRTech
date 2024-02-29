from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import json
import uuid

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
    embeddings1_np = embeddings1.detach().cpu().numpy()
    embeddings2_np = embeddings2.detach().cpu().numpy()
    similarity_scores = cosine_similarity(embeddings1_np, embeddings2_np)
    return similarity_scores.tolist()  

def match_resumes_to_vacancies(input_file, output_file):
    
    with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
    results = []
    
    for item in data:
        vacancy_uuid = item['vacancy_uuid']
        confirmed_resumes = item['confirmed_resumes']
        
        vacancy_text = item.get('vacancy_text', '')  # assuming vacancy_text might be present
        vacancy_embedding = get_embedding(vacancy_text)
        
        for resume in confirmed_resumes:
            resume_text = resume['key_info']
            resume_embedding = get_embedding(resume_text)
            
            similarity = compute_similarity(vacancy_embedding, resume_embedding)
            
            # Generate unique ID for each pair of vacancy-resume
            unique_id = str(uuid.uuid4())
            
            # Store the result
            result = {"uuid": unique_id, "vacancy_uuid": vacancy_uuid, "resume_uuid": resume['resume_uuid'], "similarity": similarity}
            results.append(result)
    
    # Write results to output file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(results, out_file)

# Путь к файлу с данными
input_file = 'text_processing/resumes_normalized.json'
output_file = 'text_processing/similaritites.json'

# Сопоставление резюме с вакансиями
match_resumes_to_vacancies(input_file, output_file)
