from django import forms


class SuggestionForm(forms.Form):
    STUD_YEAR = (
        ("y1", "سال اول"),
        ("y2", "سال دوم"),
        ("y3", "سال سوم"),
    )
    STUD_FIELD = (
        ("computer", "کامپیوتر"),
        ("chemical", "شیمیایی"),
    )
    year = forms.CharField(
        widget=forms.Select(choices=STUD_YEAR),
        required=True,
        error_messages={
            "required": "پایه تحصیلی میبایست از گزینه های موجود انتخاب شود"
        },
    )
    stud_field = forms.CharField(
        widget=forms.Select(choices=STUD_FIELD),
        required=True,
        error_messages={
            "required": "رشته تحصیلی میبایست از گزینه های موجود انتخاب شود"
        },
    )
    sug_msg = forms.CharField(
        min_length="1",
        max_length="1000",
        widget=forms.TextInput(),
        required=True,
        error_messages={
            "required": "متن انتقاد شما باید بین ۱ تا ۱۰۰۰ کاراکتر باشد",
            "min_length": "متن انتقاد شما باید بین ۱ تا ۱۰۰۰ کاراکتر باشد",
            "max_length": "متن انتقاد شما باید بین ۱ تا ۱۰۰۰ کاراکتر باشد",
        },
    )

    def clean_year(self):
        data = self.cleaned_data["year"]

        if data not in ("y1", "y2", "y3"):
            raise forms.ValidationError(
                "پایه تحصیلی میبایست از گزینه های موجود انتخاب شود"
            )

        return data

    def clean_stud_field(self):
        data = self.cleaned_data["stud_field"]

        if data not in ("computer", "chemical"):
            raise forms.ValidationError(
                "رشته تحصیلی میبایست از گزینه های موجود انتخاب شود"
            )

        return data
