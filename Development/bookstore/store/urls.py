from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('book/<int:book_id>', views.book_details, name='book_details')
]