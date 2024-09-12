from django.http import HttpResponse
from django.template.context_processors import request
from django.urls import path

from .models import GuessTheFlag
from . views import GuessTheFlagView

urlpatterns = [
    path('', GuessTheFlagView.as_view(), name='guessTheFlag'),
]