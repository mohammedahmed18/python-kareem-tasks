from task2.forms import MyForm
from django.http import HttpResponse
from django.shortcuts import render

def calculate(request):
    if(request.method == 'POST'):
        form = MyForm(request.POST)
        if form.is_valid():
           x = form.cleaned_data['first_number']
           y = form.cleaned_data['second_number']
           result = x + y
        # return HttpResponse("Result = " + str(z))
        return render(request , 'index.html' ,{
            'result' : str(result),
            'form' : form
        })

    else:
        form =  MyForm()
        return render(request , 'index.html' , {'form' : form})