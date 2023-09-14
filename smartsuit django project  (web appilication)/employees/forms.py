from django import forms
from django.forms import ModelChoiceField

from employees.models import *


class Employee_Form(forms.ModelForm):
    dob = forms.DateField(label="Date", widget=forms.TextInput(attrs={'class': 'date_picker', 'type': 'date'}))

    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'dob', 'mobile', 'gender', 'address']


class Suit_Form(forms.ModelForm):
    class Meta:
        model = Suit
        fields = ['suit_id', 'name', ]

    # def __init__(self, *args, **kwargs):
    #     super(Suit_Form, self).__init__(**kwargs)
    #     self.fields['name'].queryset = Employee.objects.filter(is_suited=False)


class Suit_Add_Form(forms.ModelForm):
    class Meta:
        model = Available_Suit
        fields = ['suit_id', 'div']


class Suit_Update_Form(forms.ModelForm):
    class Meta:
        model = Available_Suit
        fields = '__all__'