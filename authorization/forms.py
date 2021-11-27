
from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # picture = forms.FileField(
    #     widget=forms.FileInput(attrs={'class': 'form-control', 'name': 'picture'}))

    def is_valid(self):
        from authorization.services import taken_username
        data = self.data
        password: str = data.get('password')
        username: str = data.get('username')
        picture = self.files.get('picture')

        if taken_username(username):
            self.add_error('username', "This username already taken")


        # if picture.size > 10000000:
        #     self.add_error('picture', "Profile image is to big")

        return not self.errors



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control shadow-none'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control shadow-none'}))