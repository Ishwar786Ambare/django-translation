from django.urls import path
from .views import HomePageView, home

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home/', home, name='home_function')
]
