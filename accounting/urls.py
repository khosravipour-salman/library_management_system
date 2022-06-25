from django.urls import path
from accounting import views


app_name = 'accounting'

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('password_reset', views.password_reset_request, name='password_reset'),
]