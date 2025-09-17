from django.urls import path
from.views import SignUpView
from . import views


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
