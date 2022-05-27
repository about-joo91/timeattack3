from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_view, name='index-view'),
    path('',include('user.urls'))
]
