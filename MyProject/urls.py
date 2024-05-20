
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from aisearch import urls as aisearch_urls

name = 'aisearch'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(aisearch_urls, namespace = 'aisearch'))
]
