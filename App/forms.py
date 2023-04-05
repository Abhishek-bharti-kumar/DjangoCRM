from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class:form-control','placeholder:Email address',}))
    first_name = forms.CharField(label="",max_length='100',widget=forms.TextInput(attrs={'class:form-control','placeholder:First Name',}))
    last_name = forms.CharField(label="",max_length='100',widget=forms.TextInput(attrs={'class:form-control','placeholder:Last Name',}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
    
    def __init__(self, *args, **kwargs):
        super(SingUpForm,self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Conferm Password'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
