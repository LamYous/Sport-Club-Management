from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, MemberForm, CoachForm, MemberSearchForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Member, Coach
from django.db.models import Q

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'gym_app/home.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    
    return render(request, 'gym_app/login.html', {})

def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    members = Member.objects.all()
    coachs = Coach.objects.filter(is_active=True)

    total_members = members.count()
    total_male = members.filter(gender="Male").count()
    total_female = members.filter(gender="Female").count()

    last_5_members = members[:5]


    context = {
        "members":members,
        "coachs":coachs,
        "total_members":total_members,
        "total_male":total_male,
        "total_female":total_female,
        "last_5_members":last_5_members,
    }
    return render(request, 'gym_app/dashboard.html', context)

@login_required(login_url='login')
def boxing_page(request):
    members = Member.objects.all().filter(category_sport="Boxing")
    total_members= members.count()

    coach = Coach.objects.get(coach_of="Boxing")
    

    context = {
        "members": members,
        "coach":coach,
        "total_members":total_members,
        }
    return render(request, 'gym_app/boxing.html', context)

@login_required(login_url='login')
def kickboxing_page(request):
    members = Member.objects.all().filter(category_sport="Kickboxing")
    total_members = members.count()

    coach = Coach.objects.get(coach_of="Kickboxing")

    context = {
        "members": members,
        "coach":coach,
        "total_members":total_members,
        }
    return render(request, 'gym_app/kickboxing.html', context)

@login_required(login_url='login')
def mma_page(request):
    members = Member.objects.all().filter(category_sport="MMA")
    total_members = members.count()

    coach = Coach.objects.get(coach_of="MMA")

    context = {
        "members": members,
        "coach":coach,
        "total_members":total_members,
        }
    return render(request, 'gym_app/mma.html', context)

@login_required(login_url='login')
def fitness_page(request):
    members = Member.objects.all().filter(category_sport="Fitness")
    total_members = members.count()

    coach = Coach.objects.get(coach_of="Fitness")

    context = {
        "members": members,
        "coach":coach,
        "total_members":total_members,
        }
    return render(request, 'gym_app/fitness.html', context)

@login_required(login_url='login')
def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    contxt = {
        'member':member,
    }
    return render(request, 'gym_app/detail.html', contxt)

@login_required(login_url='login')
def create_member(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = MemberForm()
    return render(request, 'gym_app/create_memeber.html', {'form':form})

@login_required(login_url='login')
def update_member_info(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    return render(request, 'gym_app/update_member.html', {'form':form})

@login_required(login_url='login')
def delete_momber(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':   
        member.delete()
        return redirect('dashboard')
    return render(request, 'gym_app/delete.html', {'item':member})

@login_required(login_url='login')
def coachs_page(request):
    coachs = Coach.objects.all()
    context = {
        'coachs':coachs,
    }
    return render(request, 'gym_app/coachs.html', context)

@login_required(login_url='login')
def add_coach(request):
    form = CoachForm()
    if request.method == 'POST':
        form = CoachForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('coachs')
    else:
        form = CoachForm()

    context = {"form":form}
    return render(request, 'gym_app/create_coach.html', context)

@login_required(login_url='login')
def update_coach(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    form = CoachForm(instance=coach)
 
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coachs')
    
    context = {'form':form}
    return render(request, 'gym_app/update_coach.html', context)

@login_required(login_url='login')
def delete_coach(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        coach.delete()
        return redirect('dashboard')
    
    return render(request, 'gym_app/delete.html', {'item':coach})

@login_required(login_url='login')
def search_member(request):
    query = request.GET.get('query', '')
    result = Member.objects.none() # Start with no result  

    if query:
            result = Member.objects.filter(
                Q(first_name__icontains=query) or
                Q(last_name__icontains=query)
            )

    return render(request, 'gym_app/search_result.html', {'result':result})