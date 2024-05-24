from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import EmailVerificationView, UserLoginView, UserProfileView, UserRegistrationView, user_logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', login_required(user_logout), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
