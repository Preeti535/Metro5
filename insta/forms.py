from django import forms


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=20)
    Slocation=forms.CharField(max_length=20)

  #'  Smark=forms.IntField(required=False)