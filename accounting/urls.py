from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from accounting import views


app_name = 'accounting'

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),

    # Password reset urls
    path('password_reset/', auth_view.PasswordResetView.as_view(
        success_url=reverse_lazy('accounting:password_reset_done'),
        email_template_name='accounting/password_reset_email.txt',
        template_name='accounting/password_reset.html'), name='password_reset'),

    path('password_reset_sent/', auth_view.PasswordResetDoneView.as_view(
        # success_url=reverse_lazy('accounting:password_reset_confirm'),
        template_name='accounting/password_reset_done.html'), name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounting:password_reset_complete'),
        template_name='accounting/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='accounting/password_reset_complete.html'), name='password_reset_complete'),
]