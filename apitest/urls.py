from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView,name='ApiOverView'),
    path('item-list/',views.itemList,name='ItemList'),
    path('item-detail/<str:pk>',views.itemDetail,name='ItemDetails'),
    path('item-create/',views.itemCreate,name='ItemCreate'),
    path('item-update/<str:pk>',views.itemUpdate,name='ItemUpdate'),
    path('item-delete/<str:pk>',views.itemDelete,name='ItemDelete'),
]