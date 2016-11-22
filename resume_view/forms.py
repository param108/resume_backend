from django import forms

class ProjectForm(forms.Form):
    year = forms.CharField(max_length=4)
    title= forms.CharField(max_length=100) 
    role = forms.CharField(max_length=50)
    teamsize = forms.IntegerField()
    company = forms.CharField(max_length=50)
    desc = forms.CharField(widget=forms.Textarea)
