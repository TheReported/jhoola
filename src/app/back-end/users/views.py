from django.shortcuts import get_object_or_404, render


def dashboard(request):
    if request.user.groups.filter(name="admin-hotel").exists():
        return render(request, 'managers/dashboard-manager.html', {})
    return render(request, 'users/dashboard.html', {})


def main(request):
    return render(request, 'main.html')
