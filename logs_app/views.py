from django.shortcuts import render
from .models import LogEntry
from django.contrib.auth.decorators import login_required

@login_required
def log_list(request):
    logs = LogEntry.objects.all().order_by('-timestamp')[:100]  # last 100 logs
    return render(request, 'logs_app/log_list.html', {'logs': logs})
