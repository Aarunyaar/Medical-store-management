from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Medicine
from .forms import MedicineForm, RegisterForm

def register_view(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('medicine_list')
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_medicine(request):
    count = Medicine.objects.filter(username=request.user.username).count()
    if count >= 5:
        return render(request, 'error.html', {'message': 'You can add only 5 medicines!!'})
    
    form = MedicineForm(request.POST)
    if form.is_valid():
        medicine = form.save()
        medicine.username = request.user.username
        medicine.save()
        return redirect('medicine_list')
    
    return render(request, 'add_medicine.html', {'form': form})

@login_required
def medicine_list(request):
    search = request.GET.get('search', '')
    medicines = Medicine.objects.filter(
        username=request.user.username,
        name__icontains=search
    ).order_by('-created_at')

    paginator = Paginator(medicines, 2)
    page = request.GET.get('page')
    medicines = paginator.get_page(page)
    
    return render(request, 'medicine_list.html', {'medicines': medicines})

@login_required
def edit_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id, username=request.user.username)
    form = MedicineForm(request.POST or None, instance=medicine)
    if form.is_valid():
        form.save()
        return redirect('medicine_list')
    return render(request, 'edit_medicine.html', {'form': form})

@login_required
def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id, username=request.user.username)
    medicine.delete()
    return redirect('medicine_list')
