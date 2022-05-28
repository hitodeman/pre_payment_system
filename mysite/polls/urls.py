from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_api_ca',views.index_api_ca,name='index_api_ca'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addPayment, name='addPayment'),
    path('save/<int:T_PAYMENT_id>/', views.savePayment, name='savePayment'),
]