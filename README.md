<h2 align = center> ML TALENT MATCH</h2>
<p align = center><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Pixelify+Sans&size=30&pause=1000&color=F75D5D&vCenter=true&random=false&width=760&height=25&lines=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC+%D0%B4%D0%BB%D1%8F+%D1%81%D0%BE%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F+%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%C2%A0%D0%B8+%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B8" alt="Typing SVG" /></a></p>
<div align="justify">Алгоритм, разработанный в рамках гибридного хакатона от SENSE при поддержке Акселератора Возможностей, предназначен для оптимизации процесса определения релевантности резюме конкретной вакансии. Алгоритм позволяет рекрутерам сократить временные затраты на поиск подходящих кандидатов. 
В разработке продукта принимали участие: <a href = "https://github.com/mishantique"> Михаил Витко</a>, <a href = "https://github.com/ponyotyan"> Анастасия Ефимова</a>,<a href = "https://github.com/MrShaller"> Никита Недобежкин</a>, <a href = "https://github.com/veronikavinnichenko">Вероника Винниченко</a>.</div>

<h2 align = center> Ранжированный список кандидатов содержится в файле "SORTED_ANSWER.json"
Файл, содержащий отобранных кандидатов содержится в файле "ANSWER.json" </h2>

<!-- ROADMAP -->

<h2 align = center> Алгоритм  </h2>


<p align="center">
 <img src="https://github.com/ponyotyan/ML-TALENT/blob/main/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC.png" alt="Алгоритм"/>
</p>


## 🔧 Технологии

* ![OpenAi API](https://img.shields.io/badge/OpenAI%20API%20-%20white?logo=openai&color=black)
* ![Python](https://img.shields.io/badge/Python%20-%20white?style=plastic&logo=python&logoColor=yellow&color=%234682B4)
* ![JSON](https://img.shields.io/badge/JSON-white?logo=json&color=%239370DB)
    


## 📂 Структура проекта

sh
└── SENSE
    ├── _pycache_
    ├── .venv
    └── api_processing
       └── _pycache_
          ├── resume_processing.py
          ├── vacancies_only.json
          ├── vacancies_processing.py
    ├── JSON 
       └── JSON_processing.py
          ├── resumes_processing.json
          ├── test.json
          ├── testing_api.json
          ├── train.json
          └── vacancies_only.json
    ├── model
       ├── boosting.py
       └── random_forest.py
    ├── test_processing
       └── BERT.processing.py
       └── preprocessing.py
    ├── .env
    ├── len.py


## 📦 Для быстрого старта

<ol>
 <li> Для инициализации работы получаем уникальный токен Proxy API (загрузка переменных окружения из файла .env)</li>
 <li> Извлечение ключевой информации из json-файлов с описанием вакансий/резюме за счет Proxy API</li>
 <li> Структуризация исходных данных -> получение "uuid" и "key_info"</li>
 <li> Предобработка полученной ключевой информации с помощью нормализации, токенизации, лемматизации и удаления стоп-слов/пунктуации/символов</li>
</ol>

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| 📄 | .venv  | Файл для управления зависимостями и изоляции проекта|
| 📔 | api_processing  |Директория для работы с OpenAI API |
| 📔 | JSON |Директория, содержащая как исходные, так и предобработанные json-файлы с вакансиями/резюме |
| 📔 | model  | Директория, содержащая модели машинного обучения|
| 📔 | test_processing |  Директория, содержащая файлы с векторизацией и обработкой тестовых данных |
| 📄 | .env | Файл для настройки отдельных переменных среды |



## 🧪 Машинное обучение


<ol>
  <li>Векторизация key_info с помощью BERT для определения косинусного расстояния между ветором вакансии и соответствующего резюме (BERT.processing.py)</li>
  <li>Паралельно с BERT производится векторизация посредством TF-IDF</li>
  <li>Производится тематический анализ (topic_modeling.py) для определения роли технологического стека и оценки его влияния</li>
  <li>Используется XGBoost и Random forest для задачи классификации</li>
</ol>


### Входные данные для обучения моделей

|    |   Признак       | Тип данных |
|----|-------------------|---------------------------------------------------------------|
| 📄 | Косинусное расстояние  |Диапазон данных [-1;1]|
| 📄 | Количество образований  |Числовой признак|
| 📄 | Количество высших образований  | Числовой признак|
| 📄 | Возраст  | Исчисляется в годах|
| 📄 | Опыт работы  | Исчисляется в днях|
| 📄 | Failed resume  | Целевая перменная|



## ✔️ Эффекты от внедрения
<ul>
<li>Сокращение чел/час, затраченных на оценку релевантности вакансий</li>
<li>Минимальное участие сотрудника в процессе оценки</li>
<li>Высокая скорость работы алгоритма</li>
<li>Возможность обработки больших объемов данных</li>
</ul>


## 📊 Масштабирование
<ul>
<li>Использование алгоритма для любых резюме и вакансий, не только IT</li>
<li>Интеграция с другими сервисами для поиска работы, дополнительная прибыль</li>
<li>Использование алгоритма для работы с документооборотом компании</li>
<li>Оптимизация рабочего процесса за счет сокращение количества сотрудников, занятых сопоставлением резюме и вакансии</li>
</ul>

Мы открыты к предложениям по расширению функционала, особенно в области Machine Learning. Для внесения предложений, пожалуйста, свяжитесь с нами.

## ✉️ Контакты
Если у вас есть вопросы или предложения, свяжитесь с нами:


Telegram: 
- [@mishantique](https://t.me/mishantique) 
- [@ponyotyan](https://t.me/ponyotyan)
- [@ShallerMau](https://t.me/ShallerMau)
- [@veronika_vinnichenko](https://t.me/veronika_vinnichenko)