# Туристические места на карте (Django проект)

Проект отображает на интерактивной карте туристические локации с описанием и фотографиями. 
Пользователи могут просматривать места, их описания и изображения.

## Требования
- Python 3.13
- Установленные зависимости из `requirements.txt`

## Установка 

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-проект/репозиторий.git
cd ваш-проект
```
2.  Создайте и активируйте виртуальное окружение:
```bash
python3.13 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```
3.  Установите зависимости:
```bash
pip install -r requirements.txt
```
4.  Создайте файл  `.env`  в корне проекта со следующим содержимым:
```ini
SECRET_KEY=ваш_секретный_ключ
DEBUG=True                   
ALLOWED_HOSTS=localhost,127.0.0.1  
```
## Загрузка новых локаций
Для добавления мест используйте команду:
```bash
python manage.py load_place <URL_JSON_файла>
```
Формат JSON-файла: 
```json
{
    "title": "Название места",
    "imgs": [
        "https://url-изображения1.jpg",
        "https://url-изображения2.jpg"
    ],
    "description_short": "Краткое описание",
    "description_long": "<p>Длинное описание в HTML</p>",
    "coordinates": {
        "lng": "37.630320",
        "lat": "55.734369"
    }
}
```
