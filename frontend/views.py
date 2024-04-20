from django.shortcuts import render, get_object_or_404, redirect

from backend.forms import Job_applyForm
from backend.models import Job_category, Company_details


def index(request):
    job_categories = Job_category.objects.all()
    return render(request, 'frontend/index.html', {'job_categories': job_categories})

def home(request):
    # Retrieve all job categories from the database
    job_categories = Job_category.objects.all()
    # Retrieve all company details from the database
    company_details = Company_details.objects.all()

    # Check if a job nature filter is applied
    job_nature_filter = request.GET.get('job_nature', 'all')

    # Filter company details based on job nature if a filter is applied
    if job_nature_filter != 'all':
        company_details = company_details.filter(job_nature=job_nature_filter)

    # Pass the list of job categories and filtered company details to the template context
    return render(request, 'frontend/index.html', {'job_categories': job_categories, 'company_details': company_details})

def job_list(request):
    # Retrieve all job categories from the database
    job_categories = Job_category.objects.all()
    # Retrieve all company details from the database
    company_details = Company_details.objects.all()

    # Apply category and city filters if provided in the request
    if 'category' in request.GET and 'city' in request.GET:
        category = request.GET['category']
        city = request.GET['city']
        # Filter jobs based on selected category and city
        if category and city:
            job_categories = Job_category.objects.filter(job_category_name=category)
            company_details = company_details.filter(city__name=city)

    # Apply job nature filter if provided in the request
    job_nature_filter = request.GET.get('job_nature', 'all')
    if job_nature_filter != 'all':
        company_details = company_details.filter(job_nature=job_nature_filter)

    return render(request, 'frontend/job_list.html', {'job_categories': job_categories, 'company_details': company_details})

def job_detail(request, company_detail_id):
    company_detail = get_object_or_404(Company_details, pk=company_detail_id)
    form = Job_applyForm()

    job_categories = Job_category.objects.all()
    company_details = Company_details.objects.all()

    if request.method == 'POST':
        form = Job_applyForm(request.POST, request.FILES)
        if form.is_valid():
            job_apply_instance = form.save(commit=False)
            job_apply_instance.company_details = company_detail  # Set the company_details field
            # You also need to set the job_category field
            job_apply_instance.job_category = company_detail.job_role
            job_apply_instance.save()
            redirect_url = f'/job/{company_detail_id}/?success=true'
            return redirect(redirect_url)
    else:
        form = Job_applyForm()

        if 'category' in request.GET and 'city' in request.GET:
            category = request.GET['category']
            city = request.GET['city']
            if category and city:
                job_categories = Job_category.objects.filter(job_category_name=category)
                company_details = Company_details.objects.filter(city__name=city)

    return render(request, 'frontend/job_detail.html',
                  {'company_detail': company_detail, 'company_details': company_details,
                   'job_categories': job_categories, 'form': form})

def about(request):

    return render(request, 'frontend/about.html')


def contact(request):

    return render(request, 'frontend/contact.html')
