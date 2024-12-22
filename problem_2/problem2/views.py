from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_top_categories


def top_categories_view(request):
    data = get_top_categories()
    return JsonResponse(data, safe=False)

