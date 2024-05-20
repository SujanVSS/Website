from django.urls import path
from .views import HomePageView, InputView, OutputView

app_name = 'aisearch'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('chat/',InputView.as_view(), name = 'Chat'),
    path('result/', OutputView.as_view(), name = 'Result')
]