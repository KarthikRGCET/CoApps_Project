from django import forms
from backend.models import Country, State, City, Company_details, Job_category, Job_apply


#-----------CountryForm-----------#
class CountryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Country
        fields = ('__all__')


# -----------StateForm-----------#
class StateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StateForm, self).__init__(*args, **kwargs)

        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = State
        fields = ('__all__')


# -----------CityForm-----------#
class CityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)

        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = City
        fields = ('__all__')

#-----------job_form-----------#

class Job_categoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Job_categoryForm, self).__init__(*args, **kwargs)

        self.fields['category_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['job_category_name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Job_category
        fields = '__all__'

#-----------company_form-----------#

class Company_detailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Company_detailsForm, self).__init__(*args, **kwargs)

        self.fields['company_logo'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['url'].widget.attrs.update({'class': 'form-control'})
        self.fields['job_role'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['req_knowledge_skills_abilities'].widget.attrs.update({'class': 'form-control'})
        self.fields['education_experience'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['vacancy'].widget.attrs.update({'class': 'form-control'})
        self.fields['job_nature'].widget.attrs.update({'class': 'form-control'})
        self.fields['salary_yearly_range'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_date_apply_application'].widget.attrs.update({'class': 'form-control datepicker'})

    class Meta:
        model = Company_details
        fields = ('company_logo', 'company_name', 'email_address', 'url', 'job_role', 'company_description', 'req_knowledge_skills_abilities', 'education_experience', 'country', 'state', 'city', 'vacancy', 'job_nature', 'salary_yearly_range', 'last_date_apply_application')

#-----------job_apply-----------#

class Job_applyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Job_applyForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['degree'].widget.attrs.update({'class': 'form-control'})
        self.fields['passed_out_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['skills'].widget.attrs.update({'class': 'form-control'})
        self.fields['resume'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Job_apply
        fields = ('name', 'degree', 'passed_out_year', 'skills', 'resume')