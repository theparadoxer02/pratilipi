from django.shortcuts import render
from .forms import SendMailForm
from users.models import Profile
from .models import Theatre
from django.contrib.admin.views.decorators import staff_member_required
from .tasks import send_email_to_users_task


@staff_member_required
def sendMail(request):
    '''send mail asynchrounously to users'''
    form = SendMailForm(request.POST or None)
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            movie = form.cleaned_data.get('movie')
            subject = form.cleaned_data.get('subject')
            body = form.cleaned_data.get('body')
            theatre_ids = movie.movies.filter(is_running=True).values('theatre').distinct()
            print(theatre_ids)
            theatre_cities = Theatre.objects.filter(id__in=theatre_ids).values('city')
            user_email_list = Profile.objects.filter(city__in=theatre_cities).values_list('email', flat=True)
            # send_email_to_users_task.delay(user_email_list, body)
            print(user_email_list)
            import pdb
            # pdb.set_trace()
            return render(request, 'success_mail.html', {'user_email_list': user_email_list})
    return render(request, 'sendMail.html', {'form': form})