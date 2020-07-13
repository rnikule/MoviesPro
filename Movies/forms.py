from django import forms


class UserForm(forms.Form):
    first_name=forms.CharField(
        label= "Enter your First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your First Name'
            }
        )
    )

    last_name=forms.CharField(
        label= "Enter your Last Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Last Name'
            }
        )
    )

    username=forms.CharField(
        label= "Enter your Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Userame'
            }
        )
    )
    password=forms.CharField(
            label= "Enter your Password",
            widget=forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Your Password'
                }
            )
        )
    email=forms.EmailField(
            label= "Enter your Email",
            widget=forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Your Email'
                }
            )
        )
    mobile=forms.IntegerField(
            label= "Enter your Contact Number",
            widget=forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Your Contact Number'
                }
            )
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Enter your Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Userame'
            }
        )
    )
    password = forms.CharField(
        label="Enter your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )


