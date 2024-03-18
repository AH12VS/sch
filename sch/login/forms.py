from django import forms


class LoginForm(forms.Form):
    nat_code = forms.CharField(
        min_length="10",
        max_length="10",
        widget=forms.NumberInput(),
        required=True,
        error_messages={
            "min_length": "کد ملی باید ۱۰ رقم باشد",
            "max_length": "کد ملی باید ۱۰ رقم باشد",
            "required": "کد ملی باید ۱۰ رقم باشد",
        },
    )
    passwd = forms.CharField(
        min_length="8",
        max_length="30",
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            "min_length": "رمز عبور باید بین ۸ تا ۳۰ کاراکتر باشد",
            "max_length": "رمز عبور باید بین ۸ تا ۳۰ کاراکتر باشد",
            "required": "رمز عبور باید بین ۸ تا ۳۰ کاراکتر باشد",
        },
    )

    def clean_nat_code(self):
        data = self.cleaned_data["nat_code"]

        try:
            int(data)
        except:
            raise forms.ValidationError("کد ملی باید تنها شامل عدد باشد")

        return data
