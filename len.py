import json
with open('JSON/train.json', 'r', encoding='utf-8') as file:
    content = file.read()
    num_characters = len(content)
    print("Количество символов в файле:", num_characters)