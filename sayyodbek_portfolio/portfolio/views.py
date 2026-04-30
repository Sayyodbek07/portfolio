from django.shortcuts import render

def index(request):
    skills = [
        {'name': 'Python',      'category': 'main'},
        {'name': 'Django',      'category': 'main'},
        {'name': 'PostgreSQL',  'category': 'secondary'},
        {'name': 'Aiogram',     'category': 'secondary'},
        {'name': 'REST API',    'category': 'secondary'},
        {'name': 'Git',         'category': 'secondary'},
        {'name': 'HTML / CSS',  'category': 'secondary'},
        {'name': 'Linux',       'category': 'secondary'},
    ]

    projects = [
        {
            'title': 'Instagram Bot',
            'description': "Instagram'da avtomatik harakatlar — like, follow, xabar yuborish va boshqalar.",
            'emoji': '📸',
            'color': '#fce4ec',
            'tags': ['Python', 'Instagrapi'],
            'github': 'https://github.com/Sayyodbek07',
        },
        {
            'title': 'Rieltor Bot',
            'description': "Ko'chmas mulk e'lonlarini boshqaruvchi Telegram bot — xaridor va sotuvchi uchun.",
            'emoji': '🏠',
            'color': '#E1F5EE',
            'tags': ['Python', 'Aiogram', 'Django'],
            'github': 'https://github.com/Sayyodbek07',
        },
        {
            'title': 'iTech Landing Page',
            'description': 'Texnologiya kompaniyasi uchun zamonaviy landing page — Django backend bilan.',
            'emoji': '💻',
            'color': '#E6F1FB',
            'tags': ['Django', 'HTML/CSS'],
            'github': 'https://github.com/Sayyodbek07',
        },
    ]

    context = {
        'name': 'Sayyodbek Togayev',
        'role': 'Python Backend Developer',
        'bio': "Python bilan backend tizimlar, Telegram botlar va veb ilovalar yarataman. Kod yozish — mening tilim.",
        'skills': skills,
        'projects': projects,
        'telegram': 'https://t.me/SayyodbekTogayev',
        'github': 'https://github.com/Sayyodbek07',
        'email': 'stogayeva765@gmail.com',
    }
    return render(request, 'index.html', context)
