

from django.urls import path
from core.views import *



urlpatterns = [
    path("", home, name="home"),
    path('contact/', contact, name='contact'),
    path('article_endless/',article_endless, name='article_endless'),
    path( 'article_detail/',article_detail, name='article_detail'),
    path( 'category_hide/',category_hide, name='category_hide'),
    path('about/', about, name='about'),
    path ('login/', login, name='login'),
    path('index2/',index2,name='index2'),
    path('index_banner/',index_banner,name='index_banner'),
    path('index_custom/',index_custom,name='index_custom'),
    path('category/',category,name='category'),
    path('ui_elements/',ui_elements,name='ui_elements')

    ]