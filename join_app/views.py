from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JoinApplication

POSITIONS = [
    "Brand Protection Analyst",
    "Counterfeit Investigation Specialist",
    "Cybersecurity Specialist",
    "Client Relations Manager",
    "Research & Development Associate",
    "Marketing & Communications Specialist",
    "Other"
]

LOCATIONS = [
    "On-site (Specify location later)",
    "Remote",
    "Hybrid"
]

WORK_SCHEDULES = [
    "Full-time",
    "Part-time",
    "Contract / Freelance"
]

EXPERIENCE_YEARS = [
    "0-1 years",
    "2-4 years",
    "5+ years"
]

def join_us(request):
    if request.method == 'POST':
        # Extract form data
        form_data = request.POST
        files = request.FILES

        required_fields = ['fullName', 'email', 'phone', 'position', 'experienceYears', 'resume', 'startDate', 'whyJoin', 'dataConsent', 'termsAgree']
        missing_fields = [field for field in required_fields if not request.POST.get(field) and not request.FILES.get(field)]

        if missing_fields:
            for field in missing_fields:
                messages.error(request, f"The field '{field}' is required.")
            return render(request, 'join_app/join_team.html', {
                'form_data': form_data,
                'positions': POSITIONS,
                'locations': LOCATIONS,
                'schedules': WORK_SCHEDULES,
                'experience_options': EXPERIENCE_YEARS
            })

        # Save to DB
        JoinApplication.objects.create(
            full_name=form_data.get('fullName'),
            email=form_data.get('email'),
            phone=form_data.get('phone'),
            linkedin=form_data.get('linkedin'),
            position=form_data.get('position'),
            location=form_data.get('location'),
            experience_years=form_data.get('experienceYears'),
            skills=form_data.get('skills'),
            resume=files.get('resume'),
            cover_letter=files.get('coverLetter'),
            start_date=form_data.get('startDate'),
            work_schedule=form_data.get('workSchedule'),
            why_join=form_data.get('whyJoin'),
            unique_skills=form_data.get('uniqueSkills'),
            data_consent=True,
            terms_agree=True,
        )

        messages.success(request, "Your application has been submitted successfully.")
        return redirect('join_app:join')

    return render(request, 'join_app/join_team.html', {
        'form_data': {},
        'positions': POSITIONS,
        'locations': LOCATIONS,
        'schedules': WORK_SCHEDULES,
        'experience_options': EXPERIENCE_YEARS
    })
