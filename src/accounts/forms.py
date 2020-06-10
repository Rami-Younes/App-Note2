from django import forms
from django.contrib.auth.models import User # i use it to can change first name and last name cos django creates them
from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'headline', 'bio', 'img'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User   #meaning ,what do u want to change
        fields = [
            'username', 'first_name', 'last_name', 'email'

        ]