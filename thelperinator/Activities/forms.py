from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label="city", max_length=100)
    
class StartingPointForm(forms.Form):
    home_loc = forms.CharField(label="home_loc")