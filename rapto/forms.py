from django import forms

from .models import ContactForm



class Contact_Us_Form(forms.ModelForm):
    class Meta:
        model = ContactForm

        fields=[ 'Name','Message','Email']

        widgets = {
            'Name':forms.TextInput(attrs={'placeholder':'Your Name'}),
            'Message':forms.Textarea(attrs={'placeholder':'Your Message'}),
            'Email':forms.TextInput(attrs={'placeholder':'Your email'}),


        }