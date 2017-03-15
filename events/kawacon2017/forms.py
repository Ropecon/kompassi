# encoding: utf-8

from __future__ import unicode_literals

from django import forms

from crispy_forms.layout import Layout, Fieldset

from core.utils import horizontal_form_helper, indented_without_label
from labour.forms import AlternativeFormMixin
from labour.models import Signup, JobCategory, WorkPeriod

from .models import SignupExtra


class SignupExtraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupExtraForm, self).__init__(*args, **kwargs)
        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'shifts',
            Fieldset('Lisätiedot',
                'want_certificate',
                'shirt_size',
                'needs_lodging',
                'special_diet',
                'special_diet_other',
                'afterparty',
                'prior_experience',
                'free_text',
            )
        )


    class Meta:
        model = SignupExtra
        fields = (
            'shifts',
            'want_certificate',
            'shirt_size',
            'needs_lodging',
            'special_diet',
            'special_diet_other',
            'afterparty',
            'prior_experience',
            'free_text',
        )

        widgets = dict(
            needs_lodging=forms.CheckboxSelectMultiple,
            special_diet=forms.CheckboxSelectMultiple,
            shifts=forms.CheckboxSelectMultiple,
        )


class OrganizerSignupForm(forms.ModelForm, AlternativeFormMixin):
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        admin = kwargs.pop('admin')

        assert not admin

        super(OrganizerSignupForm, self).__init__(*args, **kwargs)

        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset('Tehtävän tiedot',
                'job_title',
            ),
        )

        self.fields['job_title'].help_text = "Mikä on tehtäväsi coniteassa?"

    class Meta:
        model = Signup
        fields = ('job_title',)

        widgets = dict(
            job_categories=forms.CheckboxSelectMultiple,
        )

    def get_excluded_m2m_field_defaults(self):
        return dict(
            job_categories=JobCategory.objects.filter(event__slug='kawacon2017', name='Conitea')
        )


class OrganizerSignupExtraForm(SignupExtraForm, AlternativeFormMixin):
    pass
