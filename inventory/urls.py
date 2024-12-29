from django.urls import path
from .views import CreateInventoryView,ListInventoryView,DeleteItemView,DetailItemView,UpdateItemView
urlpatterns = [
    path("create/",CreateInventoryView,name="create_item"),
    path("list/",ListInventoryView,name="inventory_list"),
    path("delete/<int:pk>/",DeleteItemView,name="delete_item"),
    path("detail/<int:pk>",DetailItemView,name="detail"),
    path("update/<int:pk>",UpdateItemView,name="update_item")
    
]
