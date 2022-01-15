from django import forms

# Create your forms here.


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    Company_name = forms.CharField(max_length=150)
    Upload_doc = forms.FileField()
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
