from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]

