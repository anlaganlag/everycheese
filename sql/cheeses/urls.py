from django.urls import path
from . import views

app_name ='cheese'
urlpatterns = [
    path(
            route='',
            view=views.CheeseListView.as_view(),
            name='list'
    ),

    path(
            route='<slug:slug>/',
            view=views.CheeseDetailView.as_view(),
            name='detail'
    ),
]