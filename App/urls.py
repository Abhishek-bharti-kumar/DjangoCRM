from django.urls import path
from App import views

urlpatterns = [
    path("", views.home, name='home'),
    #path("/login",views.login_user, name = "Logout-User"),
    path("logout_user/",views.logout_user, name="logout"),
    path("register_user/",views.register_user, name="register"),
]
