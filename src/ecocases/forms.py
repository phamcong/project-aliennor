from django import forms


class EcoCaseForm(forms.Form):
    ecocase_title = forms.CharField(max_length=200)
    ecocase_description = forms.CharField(
        widget=forms.Textarea, max_length=300)
    ecocase_characters = forms.CharField(
        widget=forms.Textarea, max_length=5000)
    pub_date = forms.DateTimeField('date published')
    img_url_list = forms.CharField(max_length=None)
