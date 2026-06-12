from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'full_name',
            'phone',
            'address',
            'city',
            'state',
            'pincode',
            'payment_method'
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Full Name'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '10 Digit Phone Number'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter Full Address'
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'City'
                }
            ),

            'state': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'State'
                }
            ),

            'pincode': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '6 Digit Pincode'
                }
            ),

            'payment_method': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

        }

    def clean_phone(self):

        phone = self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain digits only."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return phone

    def clean_pincode(self):

        pincode = self.cleaned_data['pincode']

        if not pincode.isdigit():
            raise forms.ValidationError(
                "Pincode must contain digits only."
            )

        if len(pincode) != 6:
            raise forms.ValidationError(
                "Pincode must be exactly 6 digits."
            )

        return pincode