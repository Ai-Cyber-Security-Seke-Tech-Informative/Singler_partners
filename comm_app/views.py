from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import Notification, NotificationReadStatus
from django.contrib import messages



def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def notification_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        message = request.POST.get('message', '').strip()

        if not title or not message:
            messages.error(request, "Title and message are required.")
        else:
            Notification.objects.create(title=title, message=message)
            messages.success(request, "Notification created successfully.")
            return redirect('comm_app:notification_list')

    return render(request, 'comm_app/notification_create.html')

@login_required
def notification_list(request):
    notifications = Notification.objects.all().order_by('-created_at')
    read_ids = NotificationReadStatus.objects.filter(user=request.user).values_list('notification_id', flat=True)
    return render(request, 'comm_app/notification_list.html', {
        'notifications': notifications,
        'read_ids': set(read_ids)
    })

@login_required
def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)

    # Mark as read if not already
    NotificationReadStatus.objects.get_or_create(user=request.user, notification=notification)

    return render(request, 'comm_app/notification_detail.html', {
        'notification': notification
    })


@login_required
def notification_delete(request, pk):
    notification = get_object_or_404(Notification, pk=pk, recipient=request.user)

    if request.method == "POST":
        notification.delete()
        return redirect('comm_app:notification_list')  # Or wherever your list is

    return render(request, 'comm_app/notification_delete.html', {
        'notification': notification
    })
