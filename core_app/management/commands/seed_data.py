from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core_app.models import Category, City, Ad, Banner


CITIES = [
    'Алматы', 'Астана', 'Шымкент', 'Қарағанды', 'Актобе',
    'Тараз', 'Павлодар', 'Өскемен', 'Семей', 'Атырау',
]

CATEGORIES = [
    'Электроника', 'Авто', 'Недвижимость', 'Одежда',
    'Мебель', 'Работа', 'Услуги', 'Животные', 'Спорт', 'Разное',
]

ADS_DATA = [
    {
        'city': 'Алматы', 'category': 'Электроника',
        'title': 'iPhone 15 Pro 256GB Titanium Black',
        'description': 'Продаю iPhone 15 Pro 256GB в идеальном состоянии. Куплен 3 месяца назад, пользовался аккуратно. Комплект полный: коробка, кабель, документы. Батарея 98%. Никаких царапин и сколов. Причина продажи — переход на Android.',
        'price': 520000, 'is_top': True,
        'image_url': 'https://images.unsplash.com/photo-1696446701796-da61225697cc?w=600&q=80',
    },
    {
        'city': 'Алматы', 'category': 'Недвижимость',
        'title': '2-комнатная квартира в Бостандыкском районе',
        'description': 'Продается просторная 2-комнатная квартира, 68 кв.м. Евроремонт 2022 года. 7 этаж из 12. Рядом метро, школы, торговые центры. Кухня-студия с новой встроенной техникой. Теплый пол в ванной.',
        'price': 35000000, 'is_top': True,
        'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=600&q=80',
    },
    {
        'city': 'Астана', 'category': 'Авто',
        'title': 'Toyota Camry 2022 года, 2.5L, белый',
        'description': 'Toyota Camry 70 кузов, 2022 год. Объем двигателя 2.5L, автомат, передний привод. Пробег 42 000 км. Один владелец. Полная комплектация: панорамная крыша, кожаный салон, подогрев сидений.',
        'price': 14500000, 'is_top': True,
        'image_url': 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=600&q=80',
    },
    {
        'city': 'Астана', 'category': 'Недвижимость',
        'title': 'Студия в ЖК Highvill Astana, 37 кв.м',
        'description': 'Сдается студия в новом ЖК. Площадь 37 кв.м. Евроремонт, мебель, бытовая техника — всё новое. Консьерж, видеонаблюдение, подземный паркинг.',
        'price': 250000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600&q=80',
    },
    {
        'city': 'Шымкент', 'category': 'Электроника',
        'title': 'Samsung Galaxy S24 Ultra 512GB',
        'description': 'Samsung Galaxy S24 Ultra, 512 GB, Titanium Gray. Состояние отличное, использовался 2 месяца. Чехол и защитное стекло в подарок. S-Pen в комплекте.',
        'price': 480000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=600&q=80',
    },
    {
        'city': 'Шымкент', 'category': 'Мебель',
        'title': 'Диван угловой Ikea LANDSKRONA, серый',
        'description': 'Угловой диван LANDSKRONA от IKEA. Цвет серый, обивка велюр. Куплен год назад. Раскладывается в кровать, есть ящик для постельного белья. Размеры: 337x222 см.',
        'price': 180000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&q=80',
    },
    {
        'city': 'Қарағанды', 'category': 'Авто',
        'title': 'Hyundai Tucson 2021, полный привод',
        'description': 'Hyundai Tucson 2021 года, 2.0L бензин, полный привод. Пробег 58 000 км. Комплектация Premium: панорамная крыша, кожаный салон, подогрев руля и сидений.',
        'price': 13200000, 'is_top': True,
        'image_url': 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=600&q=80',
    },
    {
        'city': 'Қарағанды', 'category': 'Электроника',
        'title': 'MacBook Pro 14" M3 Pro, 18GB/512GB',
        'description': 'MacBook Pro 14 дюймов с процессором M3 Pro. 18GB оперативной памяти, 512GB SSD. Space Black. Куплен в декабре 2023, на гарантии. Использовался только дома.',
        'price': 620000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&q=80',
    },
    {
        'city': 'Актобе', 'category': 'Работа',
        'title': 'Требуется Android-разработчик (удаленно)',
        'description': 'IT-компания ищет опытного Android разработчика на Kotlin. Требования: опыт от 2 лет, знание Jetpack Compose, Retrofit, Room, Coroutines. ЗП: от 400 000 тг.',
        'price': 0, 'is_top': True,
        'image_url': 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=600&q=80',
    },
    {
        'city': 'Актобе', 'category': 'Услуги',
        'title': 'Ремонт квартир под ключ — качественно',
        'description': 'Бригада опытных мастеров выполняет ремонт квартир. Косметический, капитальный, евроремонт. Электрика, сантехника, плитка, гипсокартон. Выезд на оценку бесплатно.',
        'price': 0, 'is_top': False,
        'image_url': '',
    },
    {
        'city': 'Тараз', 'category': 'Одежда',
        'title': 'Мужская куртка The North Face, размер L',
        'description': 'Зимняя куртка The North Face, оригинал. Размер L. Цвет черный. Носил один сезон. Утеплитель 550-fill гусиный пух. Отлично держит тепло до -25°C.',
        'price': 45000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1544923246-77307dd654cb?w=600&q=80',
    },
    {
        'city': 'Тараз', 'category': 'Животные',
        'title': 'Щенки лабрадора-ретривера, 2 месяца',
        'description': 'Продаются щенки лабрадора. Оба родителя с родословной. Щенки вакцинированы, обработаны от паразитов, с ветпаспортом. Характер дружелюбный. Окрас: золотой и черный.',
        'price': 120000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=600&q=80',
    },
    {
        'city': 'Павлодар', 'category': 'Спорт',
        'title': 'Велосипед горный Trek Marlin 7, 2023',
        'description': 'Горный велосипед Trek Marlin 7, размер M. Использовался одно лето. Вилка Suntour XCM, дисковые тормоза Shimano, 21-скоростная трансмиссия. Колеса 29".',
        'price': 220000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80',
    },
    {
        'city': 'Павлодар', 'category': 'Услуги',
        'title': 'Репетитор по математике и физике — ЕНТ',
        'description': 'Опытный репетитор с педагогическим стажем 8 лет. Подготовка к ЕНТ и ОГЭ. Индивидуальный подход, занятия онлайн или на дому. Пробное занятие бесплатно.',
        'price': 8000, 'is_top': False,
        'image_url': '',
    },
    {
        'city': 'Өскемен', 'category': 'Электроника',
        'title': 'PlayStation 5 + 3 геймпада + 8 игр',
        'description': 'PlayStation 5 Digital Edition. В комплекте 3 геймпада DualSense. Игры: God of War Ragnarök, Spider-Man 2, Horizon Forbidden West и другие. Всё в отличном состоянии.',
        'price': 185000, 'is_top': True,
        'image_url': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=600&q=80',
    },
    {
        'city': 'Өскемен', 'category': 'Мебель',
        'title': 'Кухонный гарнитур на заказ, белый глянец',
        'description': 'Кухонный гарнитур, МДФ крашеный, белый глянец. Встроенная техника: духовой шкаф Bosch, варочная поверхность, вытяжка. Длина 3.2 метра. Причина продажи — переезд.',
        'price': 350000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&q=80',
    },
    {
        'city': 'Семей', 'category': 'Авто',
        'title': 'Kia Sportage 2020, 2.0 бензин',
        'description': 'Kia Sportage 2020 года. 2.0L бензин, автомат, полный привод. Пробег 74 000 км. Обслуживался только в официальных СТО. Не битый, не крашеный.',
        'price': 11800000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=600&q=80',
    },
    {
        'city': 'Семей', 'category': 'Работа',
        'title': 'Фронтенд-разработчик React/Vue — вакансия',
        'description': 'Ищем фронтенд-разработчика. Требования: React или Vue от 1.5 лет, TypeScript, REST API. ЗП: от 300 000 тг. Офис или гибрид.',
        'price': 0, 'is_top': False,
        'image_url': '',
    },
    {
        'city': 'Атырау', 'category': 'Одежда',
        'title': 'Adidas Yeezy Boost 350 V2, 42 размер',
        'description': 'Кроссовки Adidas Yeezy Boost 350 V2 Zebra. Размер 42 EU. Оригинал, куплены в Дубае. Носил 3 раза, состояние идеальное. Коробка в комплекте.',
        'price': 95000, 'is_top': False,
        'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&q=80',
    },
    {
        'city': 'Атырау', 'category': 'Разное',
        'title': 'Детская коляска Bugaboo Fox 3, 2023',
        'description': 'Коляска Bugaboo Fox 3. Практически новая — использовалась 4 месяца. Цвет Midnight Black. Всесезонная, подходит с рождения. Комплект полный.',
        'price': 450000, 'is_top': False,
        'image_url': '',
    },
]


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@kaspiboard.kz', 'admin123')
            self.stdout.write(self.style.SUCCESS('Суперпользователь: admin / admin123'))

        seller, _ = User.objects.get_or_create(
            username='psychodevvv',
            defaults={
                'first_name': 'Самандар',
                'last_name': 'Айтматов',
                'email': 'sa.of2.2017@gmail.com',
            }
        )
        seller.set_password('admin123')
        seller.save()
        self.stdout.write(self.style.SUCCESS('Пользователь: psychodevvv / admin123'))

        for name in CITIES:
            City.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS(f'Городов: {City.objects.count()}'))

        for name in CATEGORIES:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS(f'Категорий: {Category.objects.count()}'))

        count = 0
        for data in ADS_DATA:
            city = City.objects.get(name=data['city'])
            category = Category.objects.get(name=data['category'])
            if not Ad.objects.filter(title=data['title']).exists():
                Ad.objects.create(
                    author=seller,
                    city=city,
                    category=category,
                    title=data['title'],
                    description=data['description'],
                    price=data['price'],
                    is_top=data['is_top'],
                    is_moderated=True,
                    image_url=data.get('image_url', ''),
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Создано объявлений: {count}'))
        self.stdout.write(self.style.SUCCESS('База данных заполнена!'))
