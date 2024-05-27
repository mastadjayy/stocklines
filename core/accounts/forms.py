from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class CustomAuthForm(AuthenticationForm):
    use_required_attribute = False

    username = UsernameField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}
    ))

    class Meta:
        error_messages = {'name': {'required': 'cannot be blank or null'}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                'username',
                css_class='mb-4'
            ),
            Div(
                'password',
                css_class='mb-4'
            ),
            Div(
                Div(
                    Submit('submit', 'Login'),
                    css_class='d-grid'
                ),
                css_class='mb-4'
            )
        )
