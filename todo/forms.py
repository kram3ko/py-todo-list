from django import forms
from todo.models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Enter content",
                    "class": "form-textarea",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-input"}
            ),
        }
