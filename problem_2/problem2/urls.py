from django.urls import path
from .views import top_categories_view

urlpatterns = [
    path('top-categories/', top_categories_view, name='top_categories'),
]
