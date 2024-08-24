from django import forms
from gest_usuario.models import Jugadores


class FormularioUsuarios(forms.Form):

	f_nickname = forms.CharField()
	f_nombre = forms.CharField()
	f_apellidos = forms.CharField()
	f_street = forms.CharField()
	f_number = forms.IntegerField()
	f_level = forms.IntegerField()
	f_door = forms.CharField()
	f_cp_code = forms.CharField()
	f_city = forms.CharField()
	f_country = forms.CharField()
	f_telefono = forms.CharField()
	f_mail = forms.EmailField()

class Login(forms.Form):

	f_nickname = forms.CharField()
	f_password = forms.CharField()

class Sign_up(forms.Form):

	f_mail = forms.EmailField()
	f_nickname = forms.CharField()
	f_password = forms.CharField()
	f_password_cnf = forms.CharField()