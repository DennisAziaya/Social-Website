from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm


# Create your views here.

def home(request):
    return render(request, 'index.html')


#
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home')
#                 else:
#                     return HttpResponse('Account Disabled')
#             else:
#                 return HttpResponse('invalid credential')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
#
#
# def user_register(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid:
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'],
#                                 email=cd['email'],
#                                 password=cd['password'])
#             user.save(commit=True)
#             return redirect('home', {'success': 'Account Successfully Created'})
#         else:
#             form = RegisterForm()
#     return render(request, 'account/register.html', {'form': form})
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
