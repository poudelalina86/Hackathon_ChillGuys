from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html');

def login(request):
    return render(request, 'login.html');

def signup(request):
    return render(request, 'signup.html');

def homepage(request):
    return render(request, 'homepage.html');

def createpost(request):
    return render(request, 'createpost.html');

def profile(request):
    return render(request, 'profile.html');