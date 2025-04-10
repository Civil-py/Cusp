from .models import Quote
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class QuoteForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TimeSheetsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Quote

        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Service': forms.Select(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', }),
            'Site_Address': forms.TextInput(attrs={'class': 'form-control', }),
            'created_date': forms.HiddenInput(),
            'last_updated': forms.HiddenInput(),
        }

        # def __init__(self, *args, **kwargs):
        #     super(QuoteForm, self).__init__(*args, **kwargs)
        #     for field in self.fields:
        #         self.fields[field].widget.attrs['class'] += ' text-white'
                # def __init__(self, *args, **kwargs):
        #     super(QuoteForm, self).__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.form_method = 'post'
        #     self.helper.add_input(Submit('submit', 'Submit'))
        #
        #     self.fields['Name'].label = 'Name'
        #     self.fields['Gross_Monthly_Salary'].label = 'Gross Monthly Salary (R)'
        #     self.fields['Black_Youth'].label = 'Black Youth (as defined by the National Youth Commission Act of 1996)'
        #



