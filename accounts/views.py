from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.core.paginator import Paginator
from django.db.models import Q
from django import forms
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile
from .forms import ProfileUpdateForm,ProfileImageUpdateForm,PasswordUpdateForm
from django.http import HttpResponseNotFound






# View for rendering home page
def index(request):
    return render(request,'index.html',{'show_services':True})

# Handles user registration by rendering and processing the registration form.
def register(request):
    if request.method=="POST":
       form = SignupForm(request.POST)
       if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect('login')
       else:
           messages.error(request,"Error")
    else:
        form = SignupForm()
        
    return render(request,'register.html',{'form':form})

# Handles user login by validating and authenticating credentials.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Corrected to pass 'user' instead of 'username'
                messages.success(request,"Login successful!")
                return redirect('index')  # Redirect to the index page after successful login
            else:
                messages.error(request, "Invalid username or password.")  # Feedback for invalid credentials
        else:
            messages.error(request, "Username and password are required.")  # Feedback for missing fields
    
    # Render the login template with additional context if needed
    return render(request, 'login.html', {'show_services': False})

# Custom Logout view that adds a success message upon logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request,"You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
    
# Handles the contact form submission and displays success or error messages
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your contact_form is submitted")
            return redirect('index')
        else:
            messages.error(request,"Please fill the fields properly")
        
    else:
        form=ContactForm()
        
    return render(request,'contact.html',{'form':form})
    
# View for rendering profile page
@login_required
def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    context = {
        'user': request.user,  # Pass the User object
        'user_profile': user_profile,  # Pass the UserProfile object
    }

    return render(request, 'profile.html', context)

# View for updating profile
@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user)
        password_form = PasswordUpdateForm(request.POST)
        image_form = ProfileImageUpdateForm(request.POST,request.FILES,instance=request.user.user_profile)
        if profile_form.is_valid() and password_form.is_valid() and image_form.is_valid():
            profile_form.save()
            
            
            new_password = password_form.cleaned_data.get('new_password1')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request,request.user)
            
        image_form.save()
            
    
            
        messages.success(request,'Your profile has been successfully updated')
        return redirect('profile_view')
    else:
        profile_form = ProfileUpdateForm(instance=request.user)
        password_form = PasswordUpdateForm()
        image_form = ProfileImageUpdateForm(instance=request.user.user_profile)
            
    return render(request,'update_profile.html',{'profile_form':profile_form,
                          'password_form': password_form,
                          'image_form': image_form})
    
# View for deleting profile    
@login_required
def delete_profile(request):
        if request.method == 'POST':
            request.user.delete()
            messages.success(request,'Your profile has been deleted')
            return redirect('index')
            
        return render(request,'delete_profile.html',{'user':request.user})
            
            





def custom_404(request, exception):
    return render(request,'404.html')