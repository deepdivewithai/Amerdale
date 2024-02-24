from django.shortcuts import redirect, render
from . import forms

# Create your views here.
def landing_page(request):
    return render(request, 'webapp/index.html')

def create_user(request):
    form = forms.CreateUserForm()

    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('webapp:home')
    
    context = {
        'form': form
    }

    return render(request, "webapp/registration.html", context)