
from django.urls import path
from . import views

urlpatterns = [

    path('index/',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('edit/',views.edit,name='edit'),
    path('show/',views.show,name='show'),
    path('editfrom/<str:u_id>/',views.editfrom,name='editfrom'),
    path('delete/<str:u_id>',views.delete,name='delete'),
]

