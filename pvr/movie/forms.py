from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Movie


class SendMailForm(forms.Form):
    movie = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('name'))
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
