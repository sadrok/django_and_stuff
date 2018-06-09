from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from userinfo.forms import UserForm, UserProfileForm
from userinfo.models import UserProfileInfo

@login_required
def index(request):
    context = {
        'title': 'Django Users',
        'users': User.objects.all(),
    }
    return render(request, 'userinfo/index.html', context)



def info(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'title': str(user),
        'user': user,
        'user_form': None,
        'profile_form': None,
    }
    return render(request, 'userinfo/info.html', context)



def edit(request, user_id):
    user = User.objects.get(id=user_id)

    result = {
        'data': 'json data here'
    }

    return JsonResponse(result)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            info = profile_form.save(commit=False)
            info.user = user

            if 'profile_pic' in request.FILES:
                info.profile_pic = request.FILES['profile_pic']

            info.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'userinfo/register.html', context)


def user_login(request):
    context = {   }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('userinfo:index'))
            else:
                return HttpResponse('Account not active')
        else:
            print(f"Someone tried to login and failed : {username}")
            return HttpResponseForbidden()

    return render(request, 'userinfo/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userinfo:index'))
