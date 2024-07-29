from django.shortcuts import render

def index(request):
    context = {
        "title": "Store Main Page",
        "sale": "Аутлет: до -70% Собственный бренд. -20% новым покупателям.",
        "is_sale": True,
    }
    
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        "title": "Store-Catalog",
        "products": [
            {
                "image": "/static/vendor/img/products/Adidas-hoodie.png",
                "cardtitle": "Худи черного цвета с монограммами adidas Originals",
                "price": 6900,
                "cardtext": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
            },
            
            {
                "image": "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                "cardtitle": "Синяя куртка The North Face",
                "price": 23750,
                "cardtext": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
            },
            
            {
                "image": "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "cardtitle": "Коричневый спортивный oversized-топ ASOS DESIGN",
                "price": 3390,
                "cardtext": "Материал с плюшевой текстурой. Удобный и мягкий.",
            },
            
            {
                "image": "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
                "cardtitle": "Черный рюкзак Nike Heritage",
                "price": 2340,
                "cardtext": "Плотная ткань. Легкий материал.",
            },
            
            {
                "image": "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
                "cardtitle": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
                "price": 13590,
                "cardtext": "Гладкий кожаный верх. Натуральный материал.",
            },
            
            {
                "image": "/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
                "cardtitle": "Темно-синие широкие строгие брюки ASOS DESIGN",
                "price": 2890,
                "cardtext": "Легкая эластичная ткань сирсакер Фактурная ткань.",
            }
        ]
    }
    
    return render(request, 'products/products.html', context)