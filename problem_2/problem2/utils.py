from django.db.models import Sum, Count
from .models import Category

def get_top_categories():
    results = (
        Category.objects.annotate(
            total_price=Sum('product__price'),
            product_count=Count('product')
        )
        .filter(total_price__isnull=False)
        .order_by('-total_price')[:5]
    )
    return [
        {
            "category_name": category.name,
            "total_price": category.total_price,
            "product_count": category.product_count,
        }
        for category in results
    ]
