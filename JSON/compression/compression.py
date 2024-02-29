import json

'''Ужимаем исходный JSON для приемлемого количества токенов 
для учета семантики'''

def process_json(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Check if 'vacancy' is a list and take the first item, or just take it directly if it's a dictionary
    vacancy = data["vacancy"][0] if isinstance(data["vacancy"], list) else data["vacancy"]
    vacancy_processed = {k: vacancy[k] for k in ["uuid", "name", "keywords", "description", "comment"]}
    
    resumes_processed = []
    for resume in data["resumes"]:
        processed_resume = {
            "uuid": resume["uuid"],
            "about": resume.get("about", ""),
            "key_skills": resume.get("key_skills", "")
        }
        
        # Last experience item
        if "experienceItem" in resume and resume["experienceItem"]:
            last_experience = resume["experienceItem"][-1]
            processed_resume["experienceItem"] = {
                "position": last_experience["position"],
                "description": last_experience["description"]
            }
        
        # First education item with specific fields
        if "educationItem" in resume and resume["educationItem"]:
            first_education = resume["educationItem"][0]
            processed_resume["educationItem"] = {
                "faculty": first_education["faculty"],
                "specialty": first_education["specialty"],
                "education_type": first_education["education_type"],
                "education_level": first_education["education_level"]
            }
        
        resumes_processed.append(processed_resume)
    
    processed_data = {
        "vacancy": vacancy_processed,
        "resumes": resumes_processed
    }
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(processed_data, file, indent=4, ensure_ascii=False)
        
# Пути к входному и выходному файлам (Резюме)
input_file = 'JSON/test.json'  
output_file = 'JSON/compression/test_compressed.json'

process_json(input_file, output_file)