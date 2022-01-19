
from django.urls import path, include

from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('forgot_password/', ForgotPasswordView.as_view()),
    # path('forgot_password_complete/', ForgotPasswordCompleteView.as_view()),
]