from app1 import views
from django.urls import path
app_name='app1'

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview',views.Listview.as_view(),name='Listview'),
    path('detailview/<int:pk>/',views.Detailview.as_view(),name='Detailview'),
    path('updateview/<int:pk>/',views.Updateview.as_view(),name='Updateview'),
]