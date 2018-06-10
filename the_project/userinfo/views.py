from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse

from userinfo.forms import UserForm, UserProfileForm


@permission_required('admin')
def index(request):
    """
    List all the users. Admin rights required
    """
    context = {
        'title': 'Django Users',
        'users': User.objects.all(),
    }
    return render(request, 'userinfo/index.html', context)


def info(request, user_id):
    """
    Show specific user's information. No permissions required
    """
    user = User.objects.get(id=user_id)
    context = {
        'title': str(user),
        'the_user': user,
        'user_form': None,
        'profile_form': None,
    }
    return render(request, 'userinfo/info.html', context)


@login_required
def edit(request, user_id):
    """
    JSON handler for Ajax editing of user information
    TODO: Figure out permission requirements
    """
    user = User.objects.get(id=user_id)

    if not request.user.is_staff and request.user.id != user.id:
        error_response = JsonResponse({"error": "You cannot edit another user's info"})
        error_response.status_code = 403
        return error_response

    result = {
        'data': user.username,
        'you': request.user.username
    }

    return JsonResponse(result)


@permission_required('admin')
def register(request):
    """
    Register a new user. Admin rights required
    """
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
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(
                    reverse('userinfo:index'))
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
