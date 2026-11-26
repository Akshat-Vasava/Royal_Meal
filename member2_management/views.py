from django.shortcuts import redirect, render


def login_view(request):
    """Render the login page and redirect to dashboard on submit (frontend-only)."""
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'member2_management/login.html')


def dashboard(request):
    """Render the Kitchen & Admin dashboard page."""
    return render(request, 'member2_management/dashboard.html')
