from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, DoctorForm
from .models import Category, Doctor
from django.contrib import messages

def index(request):
    return render(request, 'doctor/index.html')

def profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {user: user}
    return render(request, 'doctor/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('doctor:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def doctor_certification(request, pk):
    user = User.objects.get(pk=pk)
    category = Category.objects.filter(sort='DOCTOR')

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            # Category 저장
            for i in category:
                if user == i.user:
                    messages.error(request, '이미 등록!', extra_tags='alert')
                    return redirect('doctor:index')
            form.save()
            Category.objects.create(user=user, sort='DOCTOR')

            return redirect('doctor:index')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_certification.html', {
        'form': form,
    })


def individual_certification(request, pk):
    user = User.objects.get(pk=pk)
    category = Category.objects.filter(sort='INDIVIDUAL')
    for i in category:
        if user == i.user:
            messages.warning(request, '이미 등록')
            return redirect('doctor:index')
    Category.objects.create(user=user, sort='INDIVIDUAL')
    messages.success(request, '등록 완료')
    return redirect('doctor:index')

# def enterprise_certification(request, pk):
#     user = User.objects.get(pk=pk)
#     category = Category.objects.filter(sort='ENTERPRISE')
#
#     if request.method == 'POST':
#         form = EnterpriseForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = user
#
#             # Category 저장
#             for i in category:
#                 if user == i.user:
#                     messages.warning(request, '이미 등록')
#                     return redirect('doctor:index')
#             form.save()
#             Category.objects.create(user=user, sort='ENTERPRISE')
#             messages.success(request, '등록 완료')
#             return redirect('doctor:index')
#     else:
#         form = EnterpriseForm()
#     return render(request, 'doctor/enterprise_certification.html', {
#         'form': form,
#     })

def doctor_form(request, pk):
    user = User.objects.get(pk=pk)
    doctor_info = Doctor.objects.get(user=user)
    context = {
        'id': user.username,
        'name': doctor_info.name,
        'medical_name': doctor_info.medical_name,
        'address': doctor_info.address,
        'phone_number': doctor_info.phone_number,
        'license_number': doctor_info.license_number,
    }
    return render(request, 'doctor/doctor_form.html', context)


def for_user(request, pk):

    return render(request, 'doctor/for_user.html')