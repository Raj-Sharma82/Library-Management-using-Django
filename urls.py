from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_create, name='book_create'),
    path('edit/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('issue/', views.issue_list, name='issue_list'),
    path('issue/add/', views.issue_book, name='issue_book'),
    path('issue/return/<int:pk>/', views.return_book, name='return_book'),


]

