from django import forms
from .models import Task
from datetime import datetime, timedelta
from django.utils import timezone

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'due_date_time', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        now = datetime.now().date()
        if due_date and due_date < now:
            raise forms.ValidationError("Due date must be in the future")
        return due_date

    def clean_due_date_time(self):
        due_date_time = self.cleaned_data.get('due_date_time')
        due_date = self.cleaned_data.get('due_date')

        now_time = datetime.now().time()
        now_date = datetime.now().date()

        if due_date and due_date == now_date:
            if due_date_time and due_date_time < now_time:
                raise forms.ValidationError("Due date time must be in the future")
        return due_date_time
