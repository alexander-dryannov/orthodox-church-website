from django.urls import path
# from .views import HomePage
from .views import home_page


app_name = 'homepage'

urlpatterns = [
     # path('', HomePage.as_view(), name='home'),
     path('', home_page, name='home'),
     
]
