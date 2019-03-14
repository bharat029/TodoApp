from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import View
from .forms import UserRegistrationForm, UserLoginForm

class UserRegistrationFormView(View):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            messages.success(request, f'Account created for {user.username}!')
            
            return redirect('schedule:index')
            
        return render(request, self.template_name, {'form':form})
