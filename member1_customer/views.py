from django.shortcuts import render
def login_view(request):
    return render(request, 'member1_customer/login.html')

def home(request):
    return render(request, 'member1_customer/home.html')

