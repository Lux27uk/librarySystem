from django.urls import path
from django.contrib.auth import views as auth_views  # 导入 Django 内置的认证视图
from . import views

app_name = 'users'  # 定义应用的命名空间
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]