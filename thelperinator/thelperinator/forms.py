from django import forms


class StartingPointForm(forms.Form):
    home_loc = forms.CharField(label="home_loc")
    