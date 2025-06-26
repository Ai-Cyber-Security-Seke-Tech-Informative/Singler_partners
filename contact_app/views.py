from django.shortcuts import render, redirect
from .models import ContactInquiry
from django.contrib import messages

# Define your choice lists here so template can loop over them
SUBJECT_OPTIONS = [
    "General Inquiry", "Partnership Opportunity", "Request a Demo",
    "Report a Counterfeit Product", "Request Support", "Media / Press Inquiry", "Other"
]

CONTACT_METHOD_OPTIONS = ["email", "phone"]

CONTACT_TIME_OPTIONS = ["Morning", "Afternoon", "Evening"]

COUNTRY_OPTIONS = ["USA", "UK", "Kenya", "India", "Germany", "Other"]

def contact(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        errors = {}

        # Required fields
        required_fields = {
            'fullName': 'Full Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
            'privacyConsent': 'Privacy Consent',
        }

        for field, label in required_fields.items():
            if not data.get(field):
                errors[field] = f"{label} is required."

        if errors:
            return render(request, 'contact_app/contact_form.html', {
                'errors': errors,
                'form_data': data,
                'subject_options': SUBJECT_OPTIONS,
                'contact_method_options': CONTACT_METHOD_OPTIONS,
                'contact_time_options': CONTACT_TIME_OPTIONS,
                'country_options': COUNTRY_OPTIONS,
            })

        # All good – save
        contact = ContactInquiry(
            full_name=data.get('fullName'),
            email=data.get('email'),
            phone=data.get('phone'),
            company=data.get('company'),
            subject=data.get('subject'),
            contact_method=data.get('contactMethod'),
            contact_time=data.get('contactTime'),
            message=data.get('message'),
            attachment=files.get('attachment'),
            country=data.get('country'),
            city=data.get('city'),
            privacy_consent=True
        )
        contact.save()

        messages.success(request, "Form submitted successfully.")
        return redirect('contact_app:contact')

    # GET request — empty form
    return render(request, 'contact_app/contact_form.html', {
        'subject_options': SUBJECT_OPTIONS,
        'contact_method_options': CONTACT_METHOD_OPTIONS,
        'contact_time_options': CONTACT_TIME_OPTIONS,
        'country_options': COUNTRY_OPTIONS,
    })
