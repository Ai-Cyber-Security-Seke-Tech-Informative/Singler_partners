from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from django.db import IntegrityError
from join_app.models import JoinApplication
from django.shortcuts import render, get_object_or_404
from contact_app.models import ContactInquiry
from feedback_app.models import Feedback
from .models import StaffProfile
from .forms import StaffProfileUpdateForm
from .forms import AdminContactForm
from comm_app.models import Notification
from partner_app.models import PartnerInquiry
from .forms import InvitedSignupForm
from .models import InviteToken, StaffProfile
from django.db import transaction
from .serializers import StaffProfileSerializer, UserSerializer, StaffRegisterSerializer


# === API VIEWS ===

class StaffProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StaffProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.staff_profile


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class StaffRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = StaffRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User registered successfully."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# === SIGNUP VIEWS ===


def help_page(request):
    if request.method == 'POST':
        form = AdminContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully. The admin will contact you shortly.")
            return redirect('help')  # reload with a success message
    else:
        form = AdminContactForm()

    return render(request, 'auth_app/help.html', {'form': form})


def invited_signup_view(request, token):
    # Get the InviteToken or 404 if not found or already used
    invite_token = get_object_or_404(InviteToken, token=token, used=False)

    # Get the StaffProfile by email from the invite token, or show error page/message
    try:
        staff_profile = StaffProfile.objects.get(email=invite_token.email, is_verified=False)
    except StaffProfile.DoesNotExist:
        messages.error(request, "No profile found for this invitation.")
        # Redirect to a safe page like homepage or a custom error page
        return redirect('index')  # Change 'index' to your preferred safe URL name

    if request.method == 'POST':
        form = InvitedSignupForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create the user
                    user = form.save(commit=False)
                    user.username = form.cleaned_data['username']
                    user.email = form.cleaned_data['email']
                    user.set_password(form.cleaned_data['password1'])
                    user.save()

                    # Update StaffProfile with user data and mark verified
                    staff_profile.user = user
                    staff_profile.full_name = form.cleaned_data['full_name']
                    staff_profile.gender = form.cleaned_data['gender']
                    staff_profile.date_of_birth = form.cleaned_data['date_of_birth']
                    staff_profile.phone = form.cleaned_data['phone']
                    staff_profile.location = form.cleaned_data['location']
                    staff_profile.address = form.cleaned_data['address']
                    staff_profile.profile_picture = form.cleaned_data.get('profile_picture')
                    staff_profile.department = form.cleaned_data['department']
                    staff_profile.role = form.cleaned_data['role']
                    staff_profile.employment_type = form.cleaned_data['employment_type']
                    staff_profile.is_verified = True
                    staff_profile.save()

                    # Mark invite token as used
                    invite_token.used = True
                    invite_token.save()

                messages.success(request, "Signup completed successfully. You may now log in.")
                return redirect("login")

            except Exception as e:
                messages.error(request, f"Error during signup: {str(e)}")
                # Do not redirect here; instead, render the form with error message
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Prefill the form with the invitee’s email
        form = InvitedSignupForm(initial={'email': staff_profile.email})

    return render(request, "auth_app/invited_signup.html", {"form": form})

@login_required
def update_profile(request):
    profile = get_object_or_404(StaffProfile, user=request.user)

    if request.method == 'POST':
        form = StaffProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('password'):
                logout(request)
                return redirect('login')  # Make sure 'login' matches your URL name for login
            return redirect('dashboard')
    else:
        form = StaffProfileUpdateForm(instance=profile)

    return render(request, 'auth_app/update_profile.html', {'form': form})

# === AUTHENTICATION VIEWS ===

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "auth_app/loginpage.html")


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully.")
    return render(request, "auth_app/logout_page_one.html")

@login_required
def logouttwo_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully.")
    return render(request, "auth_app/logout_two.html")

@login_required
def logoutthree_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully.")
    return render(request, "auth_app/logout_three.html")



@login_required
def dashboard_view(request):
    user = request.user
    try:
        profile = user.staff_profile
    except StaffProfile.DoesNotExist:
        profile = None

    # Traemos las últimas 10 notificaciones donde el usuario es destinatario
    notifications = Notification.objects.filter(recipients=user).order_by('-created_at')[:10]

    context = {
        "full_name": profile.full_name if profile else user.get_full_name() or user.username,
        "email": profile.email if profile else user.email,
        "gender": getattr(profile, "gender", ""),
        "date_of_birth": getattr(profile, "date_of_birth", ""),
        "phone": getattr(profile, "phone", ""),
        "location": getattr(profile, "location", ""),
        "address": getattr(profile, "address", ""),
        "profile_picture": profile.profile_picture.url if profile and profile.profile_picture else "",
        "department": getattr(profile, "department", ""),
        "role": getattr(profile, "role", ""),
        "employment_type": getattr(profile, "employment_type", ""),
        "date_joined": profile.date_joined if profile else user.date_joined,
        "notifications": notifications,  # Aquí pasamos las notificaciones al template
    }
    
    return render(request, "auth_app/dashboard.html", context)


# === STATIC / PUBLIC VIEWS ===

def index_view(request):
    consent = request.COOKIES.get('cookie_consent')
    return render(request, "auth_app/index.html", {'cookie_consent': consent})


def services_view(request):
    return render(request, "auth_app/services_page.html")


def experience_view(request):
    return render(request, "auth_app/experience.html")


def ideas_view(request):
    return render(request, "auth_app/ideas.html")


def careers_view(request):
    return render(request, "auth_app/career.html")


def blog_view(request):
    return render(request, "auth_app/blog.html")


def about_view(request):
    return render(request, "auth_app/about.html")

# auth_app/views.py
@login_required
def contact_list_view(request):
    contacts = ContactInquiry.objects.order_by('-id')
    return render(request, 'auth_app/contact_list.html', {'contacts': contacts})

@login_required
def contact_detail_view(request, pk):
    contact = get_object_or_404(ContactInquiry, pk=pk)
    return render(request, 'auth_app/contact_detail.html', {'contact': contact})
@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(ContactInquiry, pk=pk)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Contact message deleted successfully.")
        return redirect("contact_list")

    return render(request, "auth_app/contact_confirm_delete.html", {"contact": contact})

@login_required
def join_list_view(request):
    applications = JoinApplication.objects.all().order_by('-id')
    return render(request, 'auth_app/join_list.html', {'applications': applications})

@login_required
def join_detail_view(request, pk):
    application = get_object_or_404(JoinApplication, pk=pk)
    return render(request, 'auth_app/join_detail.html', {'application': application})


@login_required
def join_delete(request, pk):
    application = get_object_or_404(JoinApplication, pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('auth_app:join_list')
    return render(request, 'auth_app/join_delete.html', {'application': application})


@login_required
def partner_list_view(request):
    inquiries = PartnerInquiry.objects.all().order_by('-id')
    return render(request, 'auth_app/partner_list.html', {'inquiries': inquiries})

@login_required
def partner_detail_view(request, pk):
    inquiry = get_object_or_404(PartnerInquiry, pk=pk)
    return render(request, 'auth_app/partner_detail.html', {'inquiry': inquiry})

@login_required
def partner_delete(request, pk):
    inquiry = get_object_or_404(PartnerInquiry, pk=pk)

    if request.method == 'POST':
        inquiry.delete()
        return redirect('partner_list')  # Make sure this name exists in your urls/view

    return render(request, 'auth_app/partner_delete.html', {'inquiry': inquiry})

@login_required
def feedback_list_view(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'auth_app/feedback_list.html', {'feedbacks': feedbacks})

@login_required
def feedback_detail_view(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'auth_app/feedback_detail.html', {'feedback': feedback})

@login_required
def feedback_delete(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)

    if request.method == 'POST':
        feedback.delete()
        messages.success(request, "Feedback deleted successfully.")
        return redirect('auth_app:feedback_list')

    return render(request, 'auth_app/feedback_delete.html', {'feedback': feedback})


def privacy_policy_view(request):
    return render(request, 'auth_app/policy_privacy.html')

def terms_of_service_view(request):
    return render(request, 'auth_app/terms_services.html')


@login_required
def delete_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk, recipients=request.user)

    if request.method == 'POST':
        # Optional: remove only for current user, not delete global object
        notification.recipients.remove(request.user)
        # OR delete entirely if only one user has it
        # notification.delete()

        return redirect('dashboard')  



