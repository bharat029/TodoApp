from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Schedule
from bootstrap_datepicker_plus import DateTimePickerInput
import datetime

def index(request):
    return render(request, 'schedule/index.html', {'all_schedules':sorted(request.user.schedule_set.all(), key=lambda x: x.deadline) })

class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['title', 'description', 'deadline']
    template_name = 'schedule/schedule_form.html'
    
    def get_form(self):
        form = super().get_form()
        form.fields['deadline'].widget = DateTimePickerInput()
        return form
    
    def get_success_url(self):
        return reverse_lazy('schedule:index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.deadline.date() < datetime.date.today():
            form.add_error('deadline', 'The Schedule cannot be in the past!')
            return self.form_invalid(form)
        return CreateView.form_valid(self, form)
    
class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['title', 'description', 'deadline']
    template_name = 'schedule/schedule_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.deadline.date < datetime.date.today():
            form.add_error('deadline', 'The Schedule cannot be in the past!')
            return self.form_invalid(form)
        return CreateView.form_valid(self, form)
    
    def get_success_url(self):
        return reverse_lazy('schedule:index')    
        
class ScheduleDelete(DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule:index')
