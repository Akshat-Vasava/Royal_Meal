from django.shortcuts import redirect, render


def login_view(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'member2_management/login.html')


def dashboard(request):
    return render(request, 'member2_management/dashboard.html')


def order_list(request):
    return render(request, 'member2_management/order_list.html')


def menu_manage(request):
    return render(request, 'member2_management/menu_manage.html')


def category_manage(request):
    return render(request, 'member2_management/category_manage.html')


def sales_report(request):
    return render(request, 'member2_management/sales_report.html')


def restaurant_settings(request):
    return render(request, 'member2_management/restaurant_settings.html')


def food_item_form(request):
    return render(request, 'member2_management/food_item_form.html')


def category_form(request):
    return render(request, 'member2_management/category_form.html')