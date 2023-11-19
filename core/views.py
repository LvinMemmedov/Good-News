from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def article_endless(request):
    return render(request, 'article-endless.html')


def article_detail(request):
    return render(request, 'article-detail.html')


def category_hide(request):
    return render(request, 'category-hide-navigation.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')

def index2(request):
    return render(request, 'index-2.html')


def index_banner(request):
    return render(request, 'index-banner.html')


def index_custom(request):
    return render(request, 'index-custom.html')


def category(request):
    return render(request, 'category.html')


def ui_elements(request):
    return render(request, 'ui-elements.html')










