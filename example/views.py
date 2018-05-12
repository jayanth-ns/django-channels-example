from django.contrib.auth import login as auth_login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.


User = get_user_model()


@login_required(login_url='/login/')
def user_list(request):
    """
    NOTE: This is fine for demonstration purposes, but this should be
    refactored before we deploy this app to production.
    Imagine how 100,000 users logging in and out of our app would affect
    the performance of this code!
    """
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'

    return render(request, 'example/user_list.html', {'users': users})


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(reverse('example:user_list'))
        else:
            print(form.errors)

    return render(request, 'example/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('example:login'))

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('example:login'))
        else:
            print(form.errors)
    return render(request, 'example/signup.html', {'form': form})