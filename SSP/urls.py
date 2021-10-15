from django.contrib import admin
from django.urls import path,include
from account import views as view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('register/',view.register,name='register' ),
    path('profile/',view.profile,name='profile' ),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login' ),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout' ),
]
