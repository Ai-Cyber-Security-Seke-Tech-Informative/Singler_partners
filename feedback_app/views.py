from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback

# Centralized feedback options
FEEDBACK_TYPES = [
    ('appreciation', 'Appreciation'),
    ('complaint', 'Complaint'),
    ('counterfeit', 'Report a Counterfeit Product'),
    ('suggestion', 'Suggestion'),
    ('technical', 'Technical Issue'),
]

# Define countries list here for template usage
FEEDBACK_COUNTRIES = [
    'United States',
    'United Kingdom',
    'Kenya',
    'Germany',
    'India',
    'Other',
]

def feedback(request):
    if request.method == 'POST':
        # Extract form data safely
        feedback_type = request.POST.get('feedbackType')
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # optional
        country = request.POST.get('country', '')  # optional
        city = request.POST.get('city', '')  # optional
        message_text = request.POST.get('message')
        privacy_consent = request.POST.get('privacyConsent')
        attachment = request.FILES.get('attachment')

        errors = []

        # Basic validation
        if not feedback_type:
            errors.append("Feedback type is required.")
        if not full_name:
            errors.append("Full name is required.")
        if not email:
            errors.append("Email address is required.")
        if not message_text:
            errors.append("Message is required.")
        if not privacy_consent:
            errors.append("You must consent to the privacy policy.")

        if errors:
            for error in errors:
                messages.error(request, error)

            # Pass posted data back to form, convert QueryDict to dict for safety
            form_data = request.POST.dict()
            # checkbox might not be in POST if unchecked, so ensure key presence
            form_data['privacyConsent'] = privacy_consent if privacy_consent else ''

            return render(request, 'feedback_app/feedback.html', {
                'form_data': form_data,
                'feedback_types': FEEDBACK_TYPES,
                'feedback_countries': FEEDBACK_COUNTRIES,
            })

        # Save feedback
        Feedback.objects.create(
            feedback_type=feedback_type,
            full_name=full_name,
            email=email,
            phone=phone,
            country=country,
            city=city,
            message=message_text,
            privacy_consent=True,
            attachment=attachment
        )

        messages.success(request, "Your feedback has been submitted successfully.")
        return redirect('feedback_app:feedback')

    # GET request
    return render(request, 'feedback_app/feedback.html', {
        'form_data': {},
        'feedback_types': FEEDBACK_TYPES,
        'feedback_countries': FEEDBACK_COUNTRIES,
    })
