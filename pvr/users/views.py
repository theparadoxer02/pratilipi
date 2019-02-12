from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import ProfileForm
from django.shortcuts import render, redirect
from .models import Profile
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required




# Create your views here.
@staff_member_required
def home(request):
    form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=True)
            # print(form.cleaned_data)
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # is_superuser = form.cleaned_data.get('is_superuser')
            # display_name = form.cleaned_data.get('display_name')
            # city = form.cleaned_data.get('city')
            # if raw_password == rep_password:
            #     Profile.objects.create(
            #         username=username, email=email, 
            #         city=city, display_name=display_name,
            #         is_superuser=is_superuser, password=raw_password
            #     )
            #     user = authenticate(username=username, password=raw_password)
            #     login(request, user)
            return HttpResponseRedirect('/admin')
    variables = {
        'form': form
    }
    return render(request, 'home.html', {'form': form})