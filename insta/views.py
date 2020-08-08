from django.shortcuts import render
from insta import forms
from django.http import HttpResponseRedirect
# Create your vi



def Empview(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/bye')
    else:
        form = forms.StudentForm()
    return render(request, 'myapp/happy.html', {'preethi': form})
def Thankview(request):
    return render(request, 'myapp/miss.html')