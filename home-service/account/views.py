from django.shortcuts import render
from .models import Profile


def get_profile(request):
    profile = Profile.objects.filter(user__id=request.user.id)
    return render(request, 'account/profile.html', {'profile': profile})
def login(request):
    pass

def logout(request):
    pass

def signup(request):
    pass