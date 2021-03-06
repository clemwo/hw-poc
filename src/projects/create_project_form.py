from django import forms

from .models import Project

class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'title',
            'organisation',
            'description',
            'phone_number',
            'email',
        )