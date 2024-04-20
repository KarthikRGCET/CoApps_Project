from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from backend.forms import Job_applyForm, Company_detailsForm, Job_categoryForm, CityForm, StateForm, CountryForm
from backend.models import Job_category, Job_apply, City, Country, State, Company_details


# ------- dashboard ---------#

class Dashboard(TemplateView):
    template_name = "backend/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Dashboard"  # Assigning title to the context
        context['Job_category'] = Job_category.objects.all().count
        context['company_details'] = Company_details.objects.all().count
        context['job_apply'] = Job_apply.objects.all().count
        context['city'] = City.objects.all().count
        return context


# --------country--------#

class CountryList(ListView):

    model = Country
    template_name = "backend/country/list.html"


class CountryCreate(CreateView):

    model = Country
    template_name = "backend/country/create.html"
    form_class = CountryForm
    # success_url = '/country'
    success_url = reverse_lazy('country_list')

class CountryUpdate(UpdateView):

    model = Country
    template_name = "backend/country/update.html"
    form_class = CountryForm
    # success_url = '/country'
    success_url = reverse_lazy('country_list')


class CountryDelete(DeleteView):

    model = Country
    template_name = "backend/country/delete.html"
    # success_url = '/country'
    success_url = reverse_lazy('country_list')

# --------state--------#

class StateList(ListView):

    model = State
    template_name = "backend/state/list.html"


class StateCreate(CreateView):

    model = State
    template_name = "backend/state/create.html"
    form_class = StateForm
    # success_url = '/state'
    success_url = reverse_lazy('state_list')

class StateUpdate(UpdateView):

    model = State
    template_name = "backend/state/update.html"
    form_class = StateForm
    # success_url = '/state'
    success_url = reverse_lazy('state_list')

class StateDelete(DeleteView):

    model = State
    template_name = "backend/state/delete.html"
    # success_url = '/state'
    success_url = reverse_lazy('state_list')

# --------city--------#

class CityList(ListView):

    model = City
    template_name = "backend/city/list.html"


class CityCreate(CreateView):

    model = City
    template_name = "backend/city/create.html"
    form_class = CityForm
    # success_url = '/city'
    success_url = reverse_lazy('city_list')

class CityUpdate(UpdateView):

    model = City
    template_name = "backend/city/update.html"
    form_class = CityForm
    # success_url = '/city'
    success_url = reverse_lazy('city_list')

class CityDelete(DeleteView):

    model = City
    template_name = "backend/country/delete.html"
    # success_url = '/city'
    success_url = reverse_lazy('city_list')

# --------job--------#

class Job_categoryList(ListView):

    model = Job_category
    template_name = "backend/job_category/list.html"


class Job_categoryCreate(CreateView):

    model = Job_category
    template_name = "backend/job_category/create.html"
    form_class = Job_categoryForm
    # success_url = '/job_category'
    success_url = reverse_lazy('job_category_list')

class Job_categoryUpdate(UpdateView):

    model = Job_category
    template_name = "backend/job_category/update.html"
    form_class = Job_categoryForm
    # success_url = '/job_category'
    success_url = reverse_lazy('job_category_list')

class Job_categoryDelete(DeleteView):

    model = Job_category
    template_name = "backend/job_category/delete.html"
    # success_url = '/job_category'
    success_url = reverse_lazy('job_category_list')

# --------company--------#

class Company_detailsList(ListView):

    model = Company_details
    template_name = "backend/company_details/list.html"


class Company_detailsCreate(CreateView):

    model = Company_details
    template_name = "backend/company_details/create.html"
    form_class = Company_detailsForm
    # success_url = '/company_details'
    success_url = reverse_lazy('company_details_list')

class Company_detailsUpdate(UpdateView):

    model = Company_details
    template_name = "backend/company_details/update.html"
    form_class = Company_detailsForm
    # success_url = '/company_details'
    success_url = reverse_lazy('company_details_list')

class Company_detailsDelete(DeleteView):

    model = Company_details
    template_name = "backend/company_details/delete.html"
    # success_url = '/company_details'
    success_url = reverse_lazy('company_details_list')

# --------job_apply--------#

class Job_applyList(ListView):

    model = Job_apply
    template_name = "backend/job_apply/list.html"


class Job_applyCreate(CreateView):

    model = Job_apply
    template_name = "backend/job_apply/create.html"
    form_class = Job_applyForm
    # success_url = '/backend/job_apply'
    success_url = reverse_lazy('job_apply_list')

class Job_applyUpdate(UpdateView):

    model = Job_apply
    template_name = "backend/job_apply/update.html"
    form_class = Job_applyForm
    # success_url = '/backend/job_apply'
    success_url = reverse_lazy('job_apply_list')

class Job_applyDelete(DeleteView):

    model = Job_apply
    template_name = "backend/job_apply/update.html"
    # success_url = '/backend/job_apply'
    success_url = reverse_lazy('job_apply_list')

def job_apply_count_month_wise(request):
    # Get the count of Job_apply objects grouped by month
    job_apply_data = Job_apply.objects.annotate(month=TruncMonth('posted_date')).values('month').annotate(count=Count('id'))

    # Prepare data for the line chart
    labels = [data['month'].strftime('%B %Y') for data in job_apply_data]
    counts = [data['count'] for data in job_apply_data]

    # Return data as JSON response
    return JsonResponse({'labels': labels, 'counts': counts})
