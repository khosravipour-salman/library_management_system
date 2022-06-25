from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from accounting.models import CustomUserModel
from accounting.forms import LoginForm
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
                return redirect('book:index')

    return render(request, 'accounting/sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('book:index')

