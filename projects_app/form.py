from django.forms import ModelForm
from django import forms

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'vote_total', 'vote_ratio', 'tags']
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'input input--text', 'type': 'text', 'name': 'text','id':"formInput#text", 'placeholder':field})
            
