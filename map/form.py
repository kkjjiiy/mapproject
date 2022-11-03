from django import forms
from .models import Car

class PostForm(forms.ModelForm):
	class Meta:
		model = Car
		fields= {
			'TimeStamp',
			'Latitude',
            'Longitude'
		}