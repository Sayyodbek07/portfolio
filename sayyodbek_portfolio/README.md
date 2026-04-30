# Sayyodbek Togayev — Portfolio (Django)

## O'rnatish va ishga tushirish

### 1. Virtual muhit yarating
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2. Kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 3. Serverni ishga tushiring
```bash
python manage.py runserver
```

### 4. Brauzerda oching
```
http://127.0.0.1:8000
```

---

## Ma'lumotlarni o'zgartirish

Barcha ma'lumotlar (ism, loyihalar, skilllar, havolalar) `portfolio/views.py` faylida joylashgan.

```python
context = {
    'name': 'Sayyodbek Togayev',       # <-- ismingiz
    'telegram': 'https://t.me/...',     # <-- Telegram
    'github': 'https://github.com/...', # <-- GitHub
    'email': 'siz@email.com',           # <-- Email
}
```

## Fayl tuzilmasi

```
sayyodbek_portfolio/
├── manage.py
├── requirements.txt
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py        ← ma'lumotlarni shu yerda o'zgartiring
│   └── templatetags/
│       └── custom_tags.py
├── templates/
│   └── index.html      ← dizayn shu yerda
└── static/             ← CSS/JS fayllar uchun
```
