from django import forms
from datetimewidget.widgets import DateTimeWidget
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'deadline']
        widgets = {
            #Use localization and bootstrap 3
            'deadline': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        }
