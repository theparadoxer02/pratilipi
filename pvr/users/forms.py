from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Profile

class ProfileForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    # birthdate = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'display_name', 
            'password', 'password1', 'is_superuser', 'city', 'bio')
        # fields = '__all__'