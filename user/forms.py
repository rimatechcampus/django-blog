from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username',
                               max_length=30,
                               help_text='username should not has spaces ..')
    email = forms.CharField(label='email',
                            widget=forms.EmailInput(),
                            help_text='like example@gmail.com')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1 = forms.CharField(label='password1',
                                widget=forms.PasswordInput(),
                                min_length=8)
    password2 = forms.CharField(label='password2',
                                widget=forms.PasswordInput(),
                                min_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def cleaned_password2(self):
        cd = self.cleaned_data()

        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('passords not marching ')
        return cd['password2']

    def cleaned_username(self):
        cd = self.cleaned_data()

        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('username already exists ')
        return cd['username']
