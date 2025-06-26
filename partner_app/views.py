# views.py
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PartnerInquiry

def partner_us(request):
    if request.method == 'POST':
        # Get form fields from POST data, mapping form names to model field names
        org_name = request.POST.get('orgName', '').strip()
        contact_person = request.POST.get('contactPerson', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        partnership_type = request.POST.get('partnershipType', '').strip()
        description = request.POST.get('description', '').strip()
        consent = request.POST.get('consent')

        # Get attachments (optional, single file assumed)
        attachments = request.FILES.get('attachments')

        # Validate required fields
        missing_fields = []
        if not org_name:
            missing_fields.append("Organization Name")
        if not contact_person:
            missing_fields.append("Contact Person")
        if not email:
            missing_fields.append("Email")
        if not partnership_type:
            missing_fields.append("Partnership Type")
        if not description:
            missing_fields.append("Description")
        if consent is None:
            missing_fields.append("Consent")

        if missing_fields:
            messages.error(request, f"Please complete the following fields: {', '.join(missing_fields)}")
            return render(request, 'partner_app/partner_with_us.html', {
                'form_data': request.POST,
            })

        # Save to DB with correct field names
        inquiry = PartnerInquiry(
            org_name=org_name,
            contact_person=contact_person,
            email=email,
            phone=phone if phone else None,
            partnership_type=partnership_type,
            description=description,
            consent=True,  # Since checkbox checked
        )
        if attachments:
            inquiry.attachments = attachments

        inquiry.save()

        messages.success(request, "Thank you! Your partnership inquiry was submitted successfully.")
        return redirect('partner_app:partner_us')

    return render(request, 'partner_app/partner_with_us.html')
