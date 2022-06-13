from django import forms

class MyForm(forms.Form):
    first_number = forms.IntegerField(label='number 1',required=True)
    second_number = forms.IntegerField(label='number 2',required=True)
