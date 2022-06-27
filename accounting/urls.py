from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from accounting import views


app_name = 'accounting'

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('complete-profile/', views.complete_profile, name='complete_profiel'),

    # Password change urls
    path('password-change/', auth_view.PasswordChangeView.as_view(
        success_url=reverse_lazy('accounting:password_change_done'),
        template_name='accounting/password_change.html'), name='password_change'),

    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(
        template_name='accounting/password_change_done.html'), name='password_change_done'),

    # Password reset urls
    path('password-reset/', auth_view.PasswordResetView.as_view(
        success_url=reverse_lazy('accounting:password_reset_done'),
        email_template_name='accounting/password_reset_email.txt',
        template_name='accounting/password_reset.html'), name='password_reset'),

    path('password-reset/sent/', auth_view.PasswordResetDoneView.as_view(
        # success_url=reverse_lazy('accounting:password_reset_confirm'),
        template_name='accounting/password_reset_done.html'), name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounting:password_reset_complete'),
        template_name='accounting/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password-reset_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='accounting/password_reset_complete.html'), name='password_reset_complete'),
]