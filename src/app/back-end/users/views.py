from django.shortcuts import get_object_or_404, redirect, render





def client_dashboard(request):
    if not request.user.groups.filter(name="admin-hotel").exists():
        return render(request, 'users/dashboard.html', {})


def manager_dashboard(request):
    if request.user.groups.filter(name="admin-hotel").exists():
        return render(request, 'managers/dashboard-manager.html', {})
