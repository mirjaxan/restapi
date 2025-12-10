from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
	conf_password = forms.CharField(max_length=250)
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password']

	def clean(self):
		cleaned_data = super().clean()
		password = self.cleaned_data.get('password')
		conf_password = self.cleaned_data.get('conf_password')
		username = self.cleaned_data.get('username')

		if password != conf_password:
			raise ValueError('parol va Tasdiq Parol mos kelmadi')
		
		if len(username) > 8:
			raise NameError('Username kamida 8 ta harf/ibora bolishi kerak.')
		
		return cleaned_data


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

	def clean_username(self):
		username =  self.cleaned_data.get('username')
		