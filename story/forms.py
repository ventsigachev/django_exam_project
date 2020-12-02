from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=100,
                             required=True,
                             widget=forms.TextInput(),
                             )
    country = forms.CharField(max_length=100, required=False)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
