from django.urls import path, include
from .views import StaffProfileView, UserDetailView, StaffRegisterView
from . import views


urlpatterns = [
    # Get or update the logged-in staff profile
    path('profile/', StaffProfileView.as_view(), name='staff-profile'),

    # Get basic logged-in user info (optional)
    path('user/', UserDetailView.as_view(), name='user-detail'),

    # Custom staff signup/registration endpoint
    path('register/', StaffRegisterView.as_view(), name='staff-register'),

    path('invite-signup/<uuid:token>/', views.invited_signup_view, name='invited_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-two/', views.logouttwo_view, name='logout_two'),
    path('logout-three/', views.logoutthree_view, name='logout_three'),
    

     # Static pages
    path('', views.index_view, name='index'),  
    path('dashboard/', views.dashboard_view, name='dashboard'),# Home page after login
    path('profile/update/', views.update_profile, name='update_profile'),
    path('services/', views.services_view, name='services'),
    path('experience/', views.experience_view, name='experience'),
    path('ideas/', views.ideas_view, name='ideas'),
    path('career/', views.careers_view, name='career'),
    path('blog/', views.blog_view, name='blog'),
    path('about/', views.about_view, name='about'),

    path('contact-list/', views.contact_list_view, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail_view, name='contact_detail'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),

    path('join-list/', views.join_list_view, name='join_list'),
    path('join/<int:pk>/', views.join_detail_view, name='join_detail'),
    path('join-us/delete/<int:pk>/', views.join_delete, name='join_delete'),

    # New for Partner Us
    path('partner-list/', views.partner_list_view, name='partner_list'),
    path('partner/<int:pk>/', views.partner_detail_view, name='partner_detail'),
    path('partners/<int:pk>/delete/', views.partner_delete, name='partner_delete'),

    # 👇 New Feedback URLs
    path('feedback-list/', views.feedback_list_view, name='feedback_list'),
    path('feedback/<int:pk>/', views.feedback_detail_view, name='feedback_detail'),
    path('feedback/<int:pk>/delete/', views.feedback_delete, name='feedback_delete'),

    path('notifications/', include('comm_app.urls', namespace='comm_app')),
    path('help/', views.help_page, name='help'),

    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service_view, name='terms_of_service'),

    path('notifications/delete/<int:pk>/', views.delete_notification, name='delete_notification'),


]

