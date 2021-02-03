from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='home'),
    path('add_items/', views.add_items, name='add_items'),
    path('add_category/', views.add_category, name='add_category'),
    path('list_item/', views.list_item, name='list_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    path('history/', views.list_history, name='history')
]    