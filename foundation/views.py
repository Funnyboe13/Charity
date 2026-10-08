from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import DonationForm
from .forms import VolunteerForm

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from django.shortcuts import render
from .models import Activity, Volunteer, Donation
def home(request):
    activities = Activity .objects .order_by('-date')[:5]
    total_hours = sum(a.hours for a in Activity . objects.all()) 
    total_raised = sum(d .amount for d in Donation.objects.all())
    context = {
        'activities': activities,
        'total_hours': total_hours,
        'total_raised': total_raised,
    }
    return render(request, 'foundation/home.html', context)
def about(request):
        return render(request, 'foundation/about.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'foundation/signup.html', {'form': form})

@login_required
def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.donor_name = request.user.username
            donation.save()
            return redirect('donation_success')
    else:
        form = DonationForm()
    return render(request, 'foundation/donate.html', {'form': form})
@login_required
def dashboard(request):
    total_donations = Donation.objects.count()
    total_amount = sum(d.amount for d in Donation.objects.all())
    total_volunteers = Volunteer.objects.count()
    total_activities = Activity.objects.count()
    recent_donations = Donation.objects.order_by('-date')[:10]
    my_donations = Donation.objects.filter(user=request.user).order_by('-date')
    context = {'my_donations': my_donations,
        'total_donations': total_donations,
        'total_amount': total_amount,
        'total_volunteers': total_volunteers,
        'total_activities': total_activities,
        'recent_donations': recent_donations,
    }
    return render(request, 'foundation/dashboard.html', context)
@login_required
def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'foundation/success.html')
    else:
        form = VolunteerForm()
    return render(request, 'foundation/volunteer.html', {'form': form})
def donation_success(request):
    return render(request, 'foundation/success.html')