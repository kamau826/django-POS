from django.urls import path,include
from . import views

urlpatterns=[
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('sell/<str:pk>',views.sellView,name='sell'),
    path('sellP/<str:pk>',views.sellP,name='sellP'),
    path('tables',views.tables,name='tables'),
    path('',views.index,name='index'),
    path('add-product',views.addProduct,name='add-product'),
    path('try',views.testCrispy,name='crispy'),
    path('sales/',views.sales,name='sales'),

]