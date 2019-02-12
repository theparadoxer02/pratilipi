from django.shortcuts import render
from .forms import SendMailForm
from users.models import Profile
from .models import Theatre
# Create your views here.

def sendMail(request):
    form = SendMailForm(request.POST or None)
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            movie = form.cleaned_data.get('movie')
            subject = form.cleaned_data.get('subject')
            body = form.cleaned_data.get('body')
            import pdb
            pdb.set_trace()
            theatre_ids = movie.movies.filter(is_running=True).values('theatre').distinct()
            print(theatre_ids)
            theatre_cities = Theatre.objects.filter(id__in=theatre_ids).values('city')
            user_list = Profile.objects.filter(city__in=theatre_cities).values('email', flat=True)
            print(user_list)
    return render(request, 'sendMail.html', {'form': form})