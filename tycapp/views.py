from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import tycdata
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('rohs_list')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'tycapp/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Sign up successful! Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Username already exists. Please choose another one.')
        else:
            messages.error(request, 'Invalid input. Please fill in all fields.')

    return render(request, 'tycapp/signup.html')

# Forgot Password View
def forgot_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password updated successfully! Please log in.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Username not found. Please sign up first.')
        else:
            messages.error(request, 'Invalid input. Please fill in all fields.')

    return render(request, 'tycapp/forgot_password.html')

def rohs_list(request):
    search_query = request.GET.get('q', '').strip()  # Changed 'search' to 'q'

    # Fetch all records
    data = tycdata.objects.all()

    # Apply filter if a search query is provided
    if search_query:
        data = data.filter(
            Q(requested_part__icontains=search_query) | 
            Q(te_internal_number__icontains=search_query)
        )

    # Paginate after filtering
    paginator = Paginator(data, 50)  # Show 50 rows per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'tycapp/rohs.html', context)

def reach_list(request):
    search_query = request.GET.get('q', '').strip()  # Changed 'search' to 'q'

    # Fetch all records
    data = tycdata.objects.all()

    # Apply filter if a search query is provided
    if search_query:
        data = data.filter(
            Q(requested_part__icontains=search_query) | 
            Q(te_internal_number__icontains=search_query)
        )

    # Paginate after filtering
    paginator = Paginator(data, 50)  # Show 50 rows per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'tycapp/reach.html', context)

def rohs_edit(request, pk):
    """
    View to edit a specific ROHS record.
    """
    instance = get_object_or_404(tycdata, pk=pk)  # Fetch the specific record

    if request.method == 'POST':
        # Update the instance with new data
        instance.requested_part = request.POST.get('requested_part')
        instance.te_internal_number = request.POST.get('te_internal_number')
        instance.part_status = request.POST.get('part_status')
        instance.rohs_compliant_status = request.POST.get('rohs_compliant_status')
        instance.rohs_exemption_substance_info = request.POST.get('rohs_exemption_substance_info')
        instance.save()  # Save changes to the database
        return redirect('rohs_list')  # Redirect to the list page after saving

    context = {
        'instance': instance,
    }
    return render(request, 'tycapp/rohs_edit.html', context)

def reach_edit(request, pk):
    """
    View to edit a specific ROHS record.
    """
    instance = get_object_or_404(tycdata, pk=pk)  # Fetch the specific record

    if request.method == 'POST':
        # Update the instance with new data
        instance.requested_part = request.POST.get('requested_part')
        instance.te_internal_number = request.POST.get('te_internal_number')
        instance.part_status = request.POST.get('part_status')
        instance.rohs_compliant_status = request.POST.get('reach_version_status')
        instance.rohs_compliant_status = request.POST.get('reach_compliant_status')
        instance.rohs_exemption_substance_info = request.POST.get('reach_svhc_substance')
        instance.save()  # Save changes to the database
        return redirect('rohs_list')  # Redirect to the list page after saving

    context = {
        'instance': instance,
    }
    return render(request, 'tycapp/reach_edit.html', context)

def add_tycdata(request):
    if request.method == "POST":
        requested_part = request.POST.get('requested_part')
        te_internal_number = request.POST.get('te_internal_number')
        part_status = request.POST.get('part_status')
        rohs_compliant_status = request.POST.get('rohs_compliant_status')
        rohs_exemption_substance_info = request.POST.get('rohs_exemption_substance_info')
        reach_version_status = request.POST.get('reach_version_status')
        reach_compliant_status = request.POST.get('reach_compliant_status')
        reach_svhc_substance = request.POST.get('reach_svhc_substance')

        # Save the data into the database
        tycdata.objects.create(
            requested_part=requested_part,
            te_internal_number=te_internal_number,
            part_status=part_status,
            rohs_compliant_status=rohs_compliant_status,
            rohs_exemption_substance_info=rohs_exemption_substance_info,
            reach_version_status=reach_version_status,
            reach_compliant_status=reach_compliant_status,
            reach_svhc_substance=reach_svhc_substance
        )
        return redirect('rohs_list')  # Redirect back to ROHS list page

    return render(request, 'tycapp/add_tycdata.html')
