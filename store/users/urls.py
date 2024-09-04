from django.urls import path

from users.views import login, register, profile

app_name = 'users'

#Набор уникальных путей к именам файлов для перехода на отдельные страницы
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile')
]