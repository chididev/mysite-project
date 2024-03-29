from django import forms

# Create your forms here.


# contact us form
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=200)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
