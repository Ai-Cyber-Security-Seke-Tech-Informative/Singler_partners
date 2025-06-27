from django.shortcuts import render, redirect
from .models import LogEntry
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def log_list(request):
    logs = LogEntry.objects.all().order_by('-timestamp')[:100]  # last 100 logs
    return render(request, 'logs_app/log_list.html', {'logs': logs})


@login_required
def clear_logs_view(request):
    if request.method == 'POST':
        LogEntry.objects.all().delete()
        messages.success(request, "All logs have been cleared.")
        return redirect('logs_app:logs')  # adjust if your URL name differs
    return render(request, 'logs_app/clear_logs.html')
