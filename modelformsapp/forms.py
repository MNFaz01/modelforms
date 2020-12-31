from django import forms
from modelformsapp.models import Projects
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields='__all__'
