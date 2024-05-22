from django import forms
# ya forms bnane k tariqa hai. Jis ma hum label, required,widget k bhi option mil jata hai.
class usersForm(forms.Form):
    # num 1 "Input ka name reha ga"
    num1=forms.CharField(label="Value 1", required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label="Value 2",widget=forms.TextInput(attrs={'class':"form-control"}))
    num3=forms.CharField(label="Value 3",widget=forms.TextInput(attrs={'class':"form-control"}))
