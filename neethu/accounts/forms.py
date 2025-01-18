from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from .models import UserProfile

class SignupForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email=forms.EmailField(required=True)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        
        
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This user already taken")
        return username
    
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email alrady taken")
        return email
    
    
    def clean_password2(self):
        clean_data = super().clean()
        passsword1 = clean_data.get("password1")
        password2 = clean_data.get("password2")
        if passsword1 and password2 and passsword1!=password2:
            raise forms.ValidationError("Password do not match")
        return password2
        
    

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
             
        widgets ={'name':forms.TextInput(attrs={'class':'form-control',
                                        'placeholder':'Your name'}),
          'email':forms.EmailInput(attrs={'class':'form-control',
                                        'placeholder':'Your email'}),
          'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Your Phone Number'}),
            'contact_message': forms.Textarea(attrs={'class': 'form-control',
                                                     'rows': 5, 
                                                     'placeholder': 'Your Message'}),}


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['email']
        
        
class PasswordUpdateForm(forms.Form):
    new_password1 = forms.CharField(label="New Password",
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                                            help_text="Enter a new password",)
    new_password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Re-enter the new password for confirmation.",
    )
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1!= new_password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    

class ProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
    
        
