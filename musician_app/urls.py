from django.urls import path
from . import views
urlpatterns = [
    path('musician/',views.musician,name='musician'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]
