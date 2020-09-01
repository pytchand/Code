from django.contrib import admin
from django.urls import path
from app10 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('total/',views.list_addition)
]
