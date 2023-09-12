from django import forms

g=[('male','MALE'),('female','FEMALE')]
c=[('python','python'),('django','django'),('api','api'),('selenium','selenium')]
class RegistrationForm(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Password=forms.CharField(widget=forms.PasswordInput) 
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)