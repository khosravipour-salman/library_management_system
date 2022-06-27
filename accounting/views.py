from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounting.models import CustomUserModel
from accounting.forms import LoginForm, CompleteProfileForm
from loan.models import DebtModel


def sign_up(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            debt_obj = DebtModel.objects.create(amount=0)
            CustomUserModel.objects.create(user=user_obj, debt=debt_obj)
            return redirect('accounting:sign_in')
    return render(request, 'accounting/sign_up.html', context)


def sign_in(request):
    form = LoginForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user_obj = authenticate(username=cd['username'], password=cd['password'])

            if user_obj:
                login(request, user_obj)
                # return redirect('book:index')

    return render(request, 'accounting/sign_in.html', context)


def sign_out(request):
    logout(request)
    # return redirect('book:index')


def complete_profile(request):
    user_obj = CustomUserModel.objects.get(user=request.user)
    django_user_obj = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        form = CompleteProfileForm(request.POST, instance=user_obj)

        if form.is_valid():
            cd = form.cleaned_data

            if cd['first_name']:
                django_user_obj.first_name = cd['first_name']

            if cd['last_name']:
                django_user_obj.last_name = cd['last_name']

            if cd['email']:
                django_user_obj.email = cd['email']

            if cd['age']:
                form.age = cd['age']

            if cd['phone_number']:
                form.phone_number = cd['phone_number']

            if cd['gender']:
                form.gender = cd['gender']

            if cd['address']:
                form.address = cd['address']

            if cd['national_code']:
                form.national_code = cd['national_code']

            form.save()
            django_user_obj.save()

            # return redirect('book:index')
    form = CompleteProfileForm(instance=user_obj)
    return render(request, 'accounting/complete_profile.html', {'form': form})
