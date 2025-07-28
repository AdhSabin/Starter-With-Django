from django.urls import path
from . import views

urlpatterns = [
    path('booklist',views.booklist,name='booklist'),
    path('addpublisher',views.addpublisher,name='addpublisher'),
    path('addauthor',views.addauthor,name='addauthor'),
    path('addbook',views.addbook,name='addbook'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('verify-khalti-payment/', views.verify_khalti_payment, name='verify_khalti_payment'),

]