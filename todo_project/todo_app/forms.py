from django import forms
from .models import todo_model
class TodoModelForm(forms.ModelForm):
    class Meta:
        model=todo_model
        fields='__all__'
        labels={
            "task":""
        }

class TodoEditForm(forms.Form):
    task=forms.CharField(max_length=50)




    