from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your Full Name*', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email*', 'class':'form-control'}))
    phone_no = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Your Phone*', 'class':'form-control'}))
    subject = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Subject*', 'class':'form-control'}))
    message = forms.CharField(max_length =500, widget=forms.Textarea(attrs={'placeholder': 'Your Message*', 'class':'form-control'}))
    
