from django.urls import path
from .views import clergy_page, contacts_page, donation_page


app_name = 'about'

urlpatterns = [
     path('clergy', clergy_page, name='clergy'),
     path('contacts', contacts_page, name='contacts'),
     path('donation', donation_page, name='donation'),
]
